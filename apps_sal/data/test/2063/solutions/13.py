
"""

created by shuangquan.huang at 1/13/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, W, A):
    def check(val):
        needs = [val - v for v in A]
        delta = [0 for _ in range(N)]
        water = 0
        i = 0
        curr = 0
        while i < N:
            curr += delta[i]
            if needs[i] > curr:
                w = needs[i] - curr
                water += w
                curr += w
                if i + W < N:
                    delta[i + W] -= w
                if water > M:
                    return False
            i += 1
        return water <= M

    lo, hi = min(A), max(A) + M
    while lo <= hi:
        m = (lo + hi) // 2
        if check(m):
            lo = m + 1
        else:
            hi = m - 1

    return hi


N, M, W = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, M, W, A))
