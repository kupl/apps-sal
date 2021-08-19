import numpy as np


def solve(S, N, K):
    dp = np.zeros((N + 1, 2, K + 1), dtype=np.int64)
    dp[0][0][0] = 1
    for i in range(N):
        for is_less in range(2):
            for k in range(K + 1):
                for l in range(10 if is_less else S[i] + 1):
                    k_ = k + (l > 0)
                    if k_ > K:
                        continue
                    is_less_ = is_less or l < S[i]
                    dp[i + 1][int(is_less_)][k_] += dp[i][is_less][k]
    return dp[N][0][K] + dp[N][1][K]


S = np.array([c for c in input()], dtype=np.int64)
N = len(S)
K = int(input())
print(solve(S, N, K))
