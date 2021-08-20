import numpy as np
(N, S) = map(int, input().split())
A = list(map(int, input().split()))
m = 998244353
dp = np.zeros((N + 1, S + 1), dtype=np.int64)
dp[:, 0] = [1] * (N + 1)
for (i, a) in enumerate(A):
    dp[i + 1] += dp[i]
    dp[i + 1, a:] = (dp[i + 1, a:] + dp[i, :-a]) % m
print(np.sum(dp[:, -1]) % m)
