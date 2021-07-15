#!/usr/bin/env python3
# coding: utf-8
# Last Modified: 12/Dec/19 07:21:47 PM


import sys


def main():
    n, k = get_ints()
    s = input()
    d = set(input().split())
    ans = 0
    curr = 0
    for i in range(len(s)):
        if s[i] in d:
            curr += 1
        else:
            ans += (curr * (curr + 1)) // 2
            curr = 0
    ans += (curr * (curr + 1)) // 2
    print(ans)


get_array = lambda: list(map(int, sys.stdin.readline().split()))


get_ints = lambda: list(map(int, sys.stdin.readline().split()))


input = lambda: sys.stdin.readline().strip()


def __starting_point():
    main()

__starting_point()
