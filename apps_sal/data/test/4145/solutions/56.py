from math import sqrt
x = int(input())

while True:
    f = 1
    s = int(sqrt(x))
    for i in range(2, s+1):
        if x % i == 0:
            f = 0
            break
    if f == 1:
        print(x)
        break
    x += 1
