import sys
import numpy as np
sys.setrecursionlimit(10 ** 7)
(N, T) = list(map(int, input().split()))
FOOD = [[int(x) for x in input().split()] for _ in range(N)]
FOOD.sort()
dp = np.array([np.zeros(T + 1, dtype=np.int64) for _ in range(N + 1)])
ans = 0
for i in range(N):
    (a, b) = FOOD[i]
    dp[i + 1][a:] = np.maximum(dp[i][:-a] + b, dp[i][a:])
    now = 0
    if i != N - 1:
        now = dp[i + 1][T - 1] + max(FOOD[i + 1:], key=lambda x: x[1])[1]
    ans = max(ans, now)
print(ans)
