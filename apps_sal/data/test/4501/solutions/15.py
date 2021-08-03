#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter, defaultdict


def main():
    N, A = list(map(int, input().split()))
    X = [int(x) - A for x in input().split()]

    result = Counter([0])

    for x in X:
        dct = defaultdict(int)
        for k, v in list(result.items()):
            dct[k + x] += v
        result += dct

    print((result[0] - 1))


def __starting_point():
    main()


__starting_point()
