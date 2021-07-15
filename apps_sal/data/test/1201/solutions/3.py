# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random

"""
created by shhuan at 2017/10/4 21:10

"""

N = int(input())
M = []
for i in range(N):
    M.append([int(x) for x in input().split()])

# N = 9
# M = [[13, 18, 14],
#      [8, 59, 20],
#      [9, 51, 2],
#      [18, 32, 15],
#      [1, 70, 18],
#      [14, 81, 14],
#      [10, 88, 16],
#      [18, 52, 3],
#      [1, 50, 6]]

MA = []
for i, row in enumerate(M):
    t, d, p = row
    MA.append((d, p, t, i+1))
M = sorted(MA)

# for row in M:
#     print(row)

T = [0] + [x[2] for x in M]
D = [0] + [x[0] for x in M]
P = [0] + [x[1] for x in M]
I = [0] + [x[3] for x in M]

dmax = max(D)

# dp[t][i]即时间t内能够拯救的前i个物品的最大物品价值
dp = [[0 for _ in range(N+1)] for _ in range(dmax)]
track = [[0 for _ in range(N+1)] for _ in range(dmax)]
for t in range(dmax):
    for i in range(1, N+1):
        ti = t-T[i]
        if T[i] <= t < D[i] and ti >= 0:
            dp[t][i] = max(dp[t][i-1], dp[ti][i-1] + P[i])
            if dp[t][i-1] > dp[ti][i-1]+P[i]:
                track[t][i] = (t, i-1, -1)
            else:
                track[t][i] = (ti, i-1, i)
        else:
            dp[t][i] = dp[t][i-1]
            track[t][i] = (t, i-1, -1)

# for row in dp:
#     print(row)

saved = 0
t, i, j = 0, N, -1
for j in range(dmax):
    if dp[j][N] > saved:
        saved = dp[j][N]
        t = j

print(saved)
# print(I)
res = []
while t > 0 and i > 0:
    t, i, j = track[t][i]
    if j > 0:
        res.append(I[j])

print(len(res))
print(' '.join([str(x) for x in reversed(res)]))





