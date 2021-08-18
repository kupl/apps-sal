
"""

created by shuangquan.huang at 1/14/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, K, A, pos):
    dp = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        maxx = 0
        for p in range(1, i):
            if all([pos[k][A[1][p]] < pos[k][A[1][i]] for k in range(2, K + 1)]):
                maxx = max(maxx, dp[p])
        dp[i] = maxx + 1

    return max(dp)


N, K = map(int, input().split())
A = [[0] * (N + 1)]
pos = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
for i in range(K):
    row = [0] + [int(x) for x in input().split()]
    A.append(row)
    for j, v in enumerate(row):
        pos[i + 1][v] = j

print(solve(N, K, A, pos))
