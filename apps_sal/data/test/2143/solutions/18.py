#!/usr/bin/pypy
# -*- coding: utf-8 -*-

from collections import defaultdict


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    result = defaultdict(int)
    for i in range(n):
        for j in range(i + 1, n, 1):
            result[nums[i] + nums[j]] += 1
    x = max(result.values())
    print(x)


def __starting_point():
    main()


__starting_point()
