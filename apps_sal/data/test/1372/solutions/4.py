import numpy as np


def solve(H, A, B):
    A_max = A.max()
    dp = np.zeros(H + A_max + 1, dtype=np.int64)
    for i in range(A_max + 1, H + A_max + 1):
        dp[i] = np.min(dp[i - A] + B)
    return dp[-1]


H, N, *AB = list(map(int, open(0).read().split()))
A = np.array(AB[::2], dtype=np.int64)
B = np.array(AB[1::2], dtype=np.int64)
print((solve(H, A, B)))
