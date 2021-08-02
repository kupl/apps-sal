import math
x = int(input())
while True:
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            break
    else:
        print(x)
        break
    x += 1
