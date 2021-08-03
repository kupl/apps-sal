import numpy as np

N = input()
K = int(input())

dp = np.zeros((len(N) + 1, K + 1), np.int64)
dp[1, 1] = 1
for d in range(1, len(N)):
    dp[d + 1] = dp[d]
    dp[d + 1, 1:] += dp[d, :-1]

ans = 0
for i, c in enumerate(N):
    n = len(N) - i
    if c != '0':
        ans += np.sum(dp[:n, K]) * (9 ** K)
        ans += dp[n, K] * (int(c) - 1) * (9 ** (K - 1))
        K -= 1
        if K == 0:
            ans += 1
            break

print(ans)
