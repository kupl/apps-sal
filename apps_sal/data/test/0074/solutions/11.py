import math


def prime(x):
    if x == 1:
        return False
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())

if prime(n):
    print(1)
    print(n)
elif prime(n - 2):
    print(2)
    print(n - 2, 2)
elif prime(n - 3):
    print(2)
    print(n - 3, 3)
else:
    x = n - 4
    while not prime(x):
        x -= 1

    rest = n - x

    y = rest - 1
    while not prime(y) or not prime(rest - y):
        y -= 1
    print(3)
    print(x, y, rest - y)

