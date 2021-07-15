# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/10 22:33

"""

N, M = list(map(int, input().split()))

A = [True if int(x) == 1 else False for x in input().split()]
B = [True if int(x) == 1 else False for x in input().split()]


if not A[M-1] and not B[M-1]:
    print('NO')
elif not A[0]:
    print('NO')
elif A[M-1]:
    print('YES')
else:
    if B[M-1]:
        for i in range(M, N):
            if A[i] and B[i]:
                print('YES')
                return

    print('NO')


