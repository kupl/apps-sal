# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/27 01:27

"""


N, X, K = map(int, input().split())

A = [int(x) for x in input().split()]

# consider special case firstly
if X == 1 and K == 0:
    print(0)
    return

A.sort()


def right(start):
    # find the end for [start, end] has K elements divisible by X
    x = start // X if start % X != 0 else start // X - 1
    endmin = max((x + K) * X, start)
    endmax = (x + K + 1) * X - 1

    return endmin, endmax


ans = 0
for i, v in enumerate(A):
    rmin, rmax = right(v)
    rl = bisect.bisect_left(A, rmin)
    rr = bisect.bisect_right(A, rmax)
    ans += rr - rl

print(ans)
