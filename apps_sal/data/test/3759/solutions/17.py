from math import sqrt, floor


def calc(n):
    if n == 0:
        return 1

    x = floor(sqrt(n**2 / 2))
    y = floor(sqrt(n**2 - x**2))
    if x == y:
        return x * 8
    else:
        return x * 8 + 4


n = int(input())
print(calc(n))
