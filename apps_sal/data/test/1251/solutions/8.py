# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2020/1/8 19:48

"""


def solve(A, left, right):
    s = [(left, right, 0)]
    memo = {}
    while s:
        l, r, ph = s.pop()
        h = min(A[l: r + 1])
        n = r - l + 1
        if h - ph >= n:
            memo[(l, r)] = n
            continue

        i, j = l, l
        t = []
        while j <= r:
            if A[j] == h:
                if i < j:
                    t.append((i, j - 1, h))
                i = j + 1
            j += 1
        if i <= r:
            t.append((i, r, h))

        if any([(v[0], v[1]) not in memo for v in t]):
            s.append((l, r, ph))
            s.extend(t)
        else:
            memo[(l, r)] = min(n, h - ph + sum([memo[(v[0], v[1])] for v in t] or [0]))

    return memo[left, right]


N = int(input())
A = [int(x) for x in input().split()]
print(solve(A, 0, N - 1))
