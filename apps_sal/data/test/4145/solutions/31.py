from math import sqrt
x = int(input())

while True:
    isP = True
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            isP = False
            break
    if isP:
        print (x)
        break
    x += 1
