#!/usr/bin/env python
# -*- coding:utf-8 -*-


def main():
    n, m = [int(x) for x in input().split(' ')]

    res = 0
    while True:
        if n < 0:
            res = -1
            break

        q = n // 2
        r = n % 2
        if r != 0:
            res += 1
            n -= 1
            continue

        if (q + res) % m == 0:
            res += q
            break

        res += 1
        n -= 1

    print(res)
    return


def __starting_point():
    main()


__starting_point()
