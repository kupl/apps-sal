#!/usr/bin/env python3

import sys

DEBUG = False


def read(t):
    return t(sys.stdin.readline().rstrip())


def read_list(t, sep=" "):
    return [t(s) for s in sys.stdin.readline().rstrip().split(sep)]


def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
    return


def main():
    n = read(int)
    a = read_list(int)

    ans = 0
    l = r = 0
    cur_sum = 0

    for l in range(0, n):
        if r < l:
            r = l
        while r < n and (cur_sum | a[r]) == cur_sum + a[r]:
            cur_sum += a[r]
            r += 1
        ans += r - l
        if l < r:
            cur_sum -= a[l]

    print(ans)


def __starting_point():
    main()


__starting_point()
