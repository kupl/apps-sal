#! /usr/bin/env python3

import math
import sys


def lcm(u, v):
    return u * v // math.gcd(u, v)


def main():
    n, k = list(map(int, input().split()))
    m = 1
    for i in range(1, k + 1):
        m = lcm(m, i)
        if m - 1 > n:
            print('No')
            return
    if (n + 1) % m == 0:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
