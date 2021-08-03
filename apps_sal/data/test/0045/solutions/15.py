#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math


def main():
    n, k = map(int, input().split())
    base = int(k * (k + 1) / 2)
    if n < base:
        print('-1')
        return
    closest = None
    for i in range(base, int(math.sqrt(n))):
        if n % i == 0:
            closest = i
            break
    if closest is None:
        for i in range(int(math.sqrt(n) + 1), 0, -1):
            if n % i == 0 and base <= n / i:
                closest = n / i
                break
    multiplier = int(n / closest)
    for i in range(1, k):
        print(i * multiplier, end=' ')
    print(int((k + closest - base) * multiplier))


def __starting_point():
    main()


__starting_point()
