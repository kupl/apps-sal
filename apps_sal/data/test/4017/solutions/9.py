# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/16 22:49

"""


N = int(input())

A = [int(x) for x in input().split()]

total = sum(A)
vals = collections.Counter(A)
mxVal = max(A)
ans = []

if vals[mxVal] > 1:
    for i, v in enumerate(A):
        rest = total - v
        if rest-mxVal == mxVal:
            ans.append(i+1)
else:
    for i, v in enumerate(A):
        rest = total - v
        if v == mxVal:
            second = max(max(A[:i] or [0]), max(A[i+1:] or [0]))
            if rest - second == second:
                ans.append(i+1)
        else:
            if rest - mxVal == mxVal:
                ans.append(i+1)

if ans:
    print(len(ans))
    print(' '.join(map(str, ans)))
else:
    print(0)
