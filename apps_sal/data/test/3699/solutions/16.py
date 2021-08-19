# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/16/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List

import math


def dist(posa, posb):
    return math.sqrt((posa[0] - posb[0]) ** 2 + (posa[1] - posb[1]) ** 2)


def solve(posa, posb, posc, bottles, N):
    if N == 1:
        print(min(dist(posa, bottles[0]), dist(posb, bottles[0])) + dist(posc, bottles[0]))
        return

    bottledist = [dist(posc, b) for b in bottles]
    da = [(dist(posa, bottles[i]) - bottledist[i], i) for i in range(N)]
    db = [(dist(posb, bottles[i]) - bottledist[i], i) for i in range(N)]
    d = 2 * sum(bottledist)

    heapq.heapify(da)
    heapq.heapify(db)
    a0 = heapq.heappop(da)
    b0 = heapq.heappop(db)
    ans = min(d + a0[0], d + b0[0])
    if a0[1] != b0[1]:
        ans = min(ans, d + a0[0] + b0[0])
    else:
        a1 = heapq.heappop(da)
        b1 = heapq.heappop(db)
        e = min(a0[0] + b1[0], a1[0] + b0[0])
        ans = min(ans, d + e)

    print(ans)


ax, ay, bx, by, cx, cy = list(map(int, input().split()))
N = int(input())
bottles = []
for i in range(N):
    x, y = list(map(int, input().split()))
    bottles.append((x, y))

solve((ax, ay), (bx, by), (cx, cy), bottles, N)
