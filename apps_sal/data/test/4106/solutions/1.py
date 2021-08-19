import math
import collections
import bisect
import heapq
import time
import itertools
import sys
'\ncreated by shhuan at 2018/11/17 00:27\n\n\n'
(N, K, X) = map(int, input().split())
A = [0] + [int(x) for x in input().split()]
dp = [[float('-inf') for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][X] = 0
for i in range(1, N + 1):
    for x in range(X):
        for p in range(1, K + 1):
            if i - p < 0:
                break
            if dp[i - p][x + 1] < 0:
                continue
            dp[i][x] = max(dp[i][x], dp[i - p][x + 1] + A[i])
ans = max([max(v) for v in dp[N - K + 1:]])
if ans < 0:
    print(-1)
else:
    print(ans)
