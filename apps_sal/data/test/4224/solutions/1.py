#!/usr/bin/env python3
# import sys
# sys.recursionlimit(10**7)
from functools import reduce


def divideCount(k):
    cnt = 0
    while k % 2 == 0:
        k //= 2
        cnt += 1
    return cnt


def solve(a):
    return sum(
        map(
            divideCount, a
        )
    )


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    print(('{}'.format(solve(a))))


def __starting_point():
    main()


__starting_point()
