

import os
import sys


def gcd(a, b):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b


def main():
    a, b, c, d = list(map(int, input().split()))
    if (a / c).is_integer():
        c_cnt = b // c - a // c + 1
    else:
        c_cnt = b // c - a // c
    if (a / d).is_integer():
        d_cnt = b // d - a // d + 1
    else:
        d_cnt = b // d - a // d

    lcm = c * d // gcd(max(c, d), min(c, d))
    if (a / lcm).is_integer():
        lcm_cnt = b // lcm - a // lcm + 1
    else:
        lcm_cnt = b // lcm - a // lcm
    print((b - a + 1 - c_cnt - d_cnt + lcm_cnt))


def __starting_point():
    main()


__starting_point()
