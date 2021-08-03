import numpy as np

N, T = list(map(int, input().split()))
C = [tuple(map(int, input().split())) for _ in range(N)]
C.sort(key=lambda x: x[0])

dp = np.zeros(T, dtype=int)
ans = 0
for i, (a, b) in enumerate(C):
    ans = max(ans, dp[T - 1] + b)
    new_dp = dp.copy()
    new_dp[a:] = np.maximum(dp[a:], dp[:-a] + b)
    dp = new_dp
print(ans)
