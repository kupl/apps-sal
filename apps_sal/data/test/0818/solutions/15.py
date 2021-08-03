from fractions import gcd
from random import randint


def __starting_point():
    n = int(input())
    if n < 3:
        print(-1)
        return
    res = (210 - (10**(n - 1) % 210)) + 10**(n - 1)
    print(res)


__starting_point()
