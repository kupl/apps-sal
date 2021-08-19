# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/12/15 22:40

"""


def check(val):
    l, r = 0, len(val) - 1

    while l < r:
        if val[l] != val[r]:
            return True
        l += 1
        r -= 1

    return False


T = int(input())
for ti in range(T):
    s = list(input())
    s.sort()
    if check(s):
        print(''.join(s))
    else:
        print(-1)
