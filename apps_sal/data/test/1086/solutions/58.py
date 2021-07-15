
import sys
from collections import defaultdict
from collections import deque
import numpy as np
import heapq
from heapq import heappush, heappop
import itertools
import math
import copy

H, W = list(map(int, input().split()))

A = []
B = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)

for _ in range(H):
    b = list(map(int, input().split()))
    B.append(b)

C = []
for i in range(H):
    cs = []
    for j in range(W):
        c = abs(A[i][j] - B[i][j])
        cs.append(c)

    C.append(cs)


X = (H+W) * 80
L = X + X + 1

dp = [[0] * W for _ in range(H)]
dp[0][0] = np.zeros(L, np.bool)
d = C[0][0]
dp[0][0][X+d] = 1
dp[0][0][X-d] = 1

for r in range(H):
    for c in range(W):
        if r == 0 and c == 0:
            continue

        l = np.zeros(L, np.bool)
        d = C[r][c]

        if r != 0:
            l[d:] |= dp[r-1][c][:L-d]
            l[:L-d] |= dp[r-1][c][d:]

        if c != 0:
            l[d:] |= dp[r][c-1][:L-d]
            l[:L-d] |= dp[r][c-1][d:]

        dp[r][c] = l

dp = dp[-1][-1]
d = np.where(dp)[0] - X
ans = np.abs(d).min()
print(ans)

