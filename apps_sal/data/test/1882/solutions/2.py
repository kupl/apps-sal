# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/11/18

"""

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

N, T = list(map(int, input().split()))
#
# N, T = 200000, 1000000000

ta = []
for i in range(N):
    a, t = list(map(int, input().split()))
    ta.append((t, a, i + 1))
    # ta.append((10000, 200000, i+1))

ta.sort()


score = 0
solvedCount = 0
aks = []
heapq.heapify(aks)
sc = collections.defaultdict(list)
for i in range(N):
    t, a, _ = ta[i]
    if T < t:
        break

    T -= t
    solvedCount += 1

    sc[a].append((t, i))
    heapq.heappush(aks, a)
    removed = []
    while aks and aks[0] < solvedCount:
        k = heapq.heappop(aks)
        removed.append(k)
        v = sc[k]
        solvedCount -= len(v)
        for _, j in v:
            T += ta[j][0]
        del sc[k]

    score = max(score, solvedCount)


print(score)
print(score)

vta = [(t, a, i) for t, a, i in ta if a >= score]
vta.sort()
ans = [i for _, _, i in vta[:score]]
print(" ".join(map(str, ans)))
