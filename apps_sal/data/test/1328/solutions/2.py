import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools

N, Ma, Mb = map(int, input().split())

DP = [[10**9 for _ in range(401)] for _ in range(401)]
DP[0][0] = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    for i in range(401)[::-1]:
        for j in range(401)[::-1]:
            if DP[i][j] != 10**9:
                DP[i + a][j + b] = min(DP[i + a][j + b], DP[i][j] + c)

ans = 10**9
A, B = Ma, Mb
while max(A, B) <= 400:
    ans = min(ans, DP[A][B])
    A += Ma
    B += Mb

if ans == 10**9:
    print(-1)
else:
    print(ans)
