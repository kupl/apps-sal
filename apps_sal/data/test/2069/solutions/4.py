#!/usr/bin/env python3


import sys


def solver():
    import re
    lines = iter(sys.stdin.read().split('\n'))
    n, m = tuple(map(int, next(lines).split(' ')))
    revp = [0, ] * (n + 1)
    for i, val in enumerate(map(int, next(lines).split(' '))):
        revp[val] = i
    pairs = [-1] * (n + 1)
    pairs[-1] = n - 1
    for i in range(m):
        a, b = tuple(map(int, next(lines).split(' ')))
        a, b = revp[a], revp[b]
        if b > a:
            a, b = b, a
        pairs[a] = max(pairs[a], b)
    res = 0
    pos = 0
    for right, left in enumerate(pairs):
        if left == -1:
            continue
        for i in range(pos, left + 1):
            res = res + right - i
        pos = max(pos, left + 1)
    return res


def main():
    res = solver()
    sys.stdout.write("{}\n".format(res))
    return 0


def __starting_point():
    main()


__starting_point()
