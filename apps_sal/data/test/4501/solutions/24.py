import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

N, A = map(int, input().split())
X = list(map(int, input().split()))

dp = [[0] * (N * A + 1) for _ in range(N + 1)]

dp[0][0] = 1

for i in range(0, N):
    for cnt in range(N, 0, -1):
        for val in range(N * A, -1, -1):
            if val - X[i] >= 0:
                dp[cnt][val] += dp[cnt - 1][val - X[i]]

ans = 0
for i in range(1, N + 1):
    ans += dp[i][i * A]

print(ans)
