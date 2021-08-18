
"""

created by shuangquan.huang at 1/20/20

"""

import collections
import time
import os
import sys
import bisect
import heapq
from typing import List


def solve(N, M, T, edges):
    g = collections.defaultdict(list)
    for u, v, t in edges:
        g[u].append((v, t))

    dp = [[T + 1 for _ in range(N + 1)] for _ in range(N + 1)]
    pre = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    dp[1][1] = 0
    pre[1][1] = 0

    q = [(1, 1, 0)]
    while q:
        nq = []
        for city, dist, pcost in q:
            dist += 1
            for dest, ncost in g[city]:
                cost = pcost + ncost
                if cost <= T and dp[dest][dist] > cost:
                    dp[dest][dist] = cost
                    pre[dest][dist] = city
                    nq.append((dest, dist, cost))
        q = nq

    ans = max([i for i in range(N, -1, -1) if dp[N][i] <= T])
    print(ans)

    path = []
    k = N
    l = ans
    while k:
        path.append(k)
        k = pre[k][l]
        l -= 1

    print(' '.join(map(str, path[::-1])))


N, M, T = map(int, input().split())
edges = []
for i in range(M):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

solve(N, M, T, edges)
