# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2/11/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(x0, y0, x1, y1, N, A):
    points = set()
    for y, xl, xr in A:
        for x in range(xl, xr + 1):
            points.add((x, y))
    dist = collections.defaultdict(int)

    q = [(x0, y0)]
    while q:
        nq = []
        for x, y in q:
            d = dist[x, y] + 1
            for ny in range(y - 1, y + 2):
                for nx in range(x - 1, x + 2):
                    if (nx, ny) in points and (dist[nx, ny] == 0 or dist[nx, ny] > d):
                        dist[nx, ny] = d
                        nq.append((nx, ny))
        q = nq

    # print(dist)
    # print(points)

    ans = dist[x1, y1]
    return ans if ans != 0 else -1


y0, x0, y1, x1 = map(int, input().split())
N = int(input())
A = []
for i in range(N):
    y, xl, xr = map(int, input().split())
    A.append((y, xl, xr))

print(solve(x0, y0, x1, y1, N, A))
