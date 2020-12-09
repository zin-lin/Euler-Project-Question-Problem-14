import random
x,z,y = ["Loading","loading"],[],['.                ','..               ',"..               ","......           ","........         ",
                                  ".................","...              "]
print(random.choice(x)+random.choice(y))
for i in range(1000000):
    test ,a = 0, i
    while 1:
        if a%2 == 0:a = a/2
        else:a = (3*a)+1
        test += 1
        if a<2 or a ==1:break
    z.append(test)
    i+= 1
print(z[837799])
print("Ans- ",z.index(max(z)))