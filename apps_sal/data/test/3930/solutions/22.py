# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 1/10/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K, A):
    presum = [0 for _ in range(N + 1)]
    vi = collections.defaultdict(list)
    for i, v in enumerate(A):
        presum[i + 1] = presum[i] + v
    for i, v in enumerate(presum):
        vi[v].append(i)

    maxval = max(presum)
    minval = min(presum)
    ans = 0
    for i, v in enumerate(presum):
        us = []
        if K > 1:
            c = 0
            u = v + 1
            while u <= maxval:
                us.append(u)
                c += 1
                u = v + K ** c
        elif K < -1:
            # even
            c = 0
            u = v + 1
            while u <= maxval:
                us.append(u)
                c += 2
                u = v + K ** c

            c = 1
            u = v + K
            while u >= minval:
                us.append(u)
                c += 2
                u = v + K ** c
        elif K == 1:
            us = [v + 1]
        elif K == -1:
            us = [v + 1, v - 1]

        for u in us:
            if u in vi:
                idx = vi[u]
                ans += len(idx) - bisect.bisect_right(idx, i)

    return ans


N, K = map(int, input().split())
A = [int(x) for x in input().split()]
print(solve(N, K, A))
