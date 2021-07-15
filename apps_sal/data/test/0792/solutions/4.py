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
created by shhuan at 2017/11/24 00:20

"""

N, D = map(int, input().split())
A = [int(x) for x in input().split()]

presum = [0] * (N+1)

for i in range(1, N+1):
    presum[i] = presum[i-1] + A[i-1]

rightmax = [0] * N
mx = float('-inf')
for i in range(N-1, -1, -1):
    mx = max(mx, presum[i+1])
    rightmax[i] = mx

# print(presum)
# print(rightmax)

if any(v > D for v in presum):
    print(-1)
    return

ans = 0
added = 0
for i in range(N):
    if A[i] == 0:
        if presum[i+1] + added < 0:
            dmin = 0-presum[i+1]-added
            dmax = min(D-presum[i+1]-added, D-added-rightmax[i])
            if dmin > dmax:
                print(-1)
                return

            added += dmax
            ans += 1
print(ans)
