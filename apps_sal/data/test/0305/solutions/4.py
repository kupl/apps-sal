#!/usr/bin/env python3
# coding: utf-8
# Last Modified: 15/Dec/19 02:48:07 PM


import sys


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    ans = 0
    if e > f:
        ans = e * min(a, d)
        x = min(a, d)
        a -= x
        d -= x
        ans += f * min(b, c, d)
        print(ans)
    else:
        ans += f * min(b, c, d)
        x = min(b, c, d)
        b -= x
        c -= x
        d -= x
        ans += e * min(a, d)
        print(ans)


get_array = lambda: list(map(int, sys.stdin.readline().split()))


get_ints = lambda: list(map(int, sys.stdin.readline().split()))


input = lambda: sys.stdin.readline().strip()


def __starting_point():
    main()

__starting_point()
