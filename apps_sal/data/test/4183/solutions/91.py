

import os
import sys


def gcd(a, b):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b


def main():
    n = int(input())
    ans = int(input())
    for _ in range(n - 1):
        t = int(input())
        ans = ans * t // gcd(max(ans, t), min(ans, t))
    print(ans)


def __starting_point():
    main()


__starting_point()
