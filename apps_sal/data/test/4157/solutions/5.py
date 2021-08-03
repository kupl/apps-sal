#!/usr/bin/env python3

import collections


def solve(n, xs):
    ys = set(xs)
    zs = collections.deque()
    zs.append(ys.pop())
    while ys:
        x = zs[len(zs) - 1]
        if x // 3 in ys:
            ys.remove(x // 3)
            zs.append(x // 3)
        elif 2 * x in ys:
            ys.remove(2 * x)
            zs.append(2 * x)
        else:
            break
    while ys:
        x = zs[0]
        if x // 2 in ys:
            ys.remove(x // 2)
            zs.appendleft(x // 2)
        elif 3 * x in ys:
            ys.remove(3 * x)
            zs.appendleft(3 * x)
        else:
            break
    return zs


def main():
    n = int(input())
    xs = [int(x) for x in input().split()]
    print(*solve(n, xs))


def __starting_point():
    main()


__starting_point()
