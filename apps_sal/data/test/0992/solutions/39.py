from copy import copy
import numpy as np
N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = np.zeros(S + 100, np.int64)
dp[0] = 1
for i in range(N):
    buf = copy(dp)
    dp = 2 * dp
    dp[A[i]:] += buf[:-A[i]]
    dp %= 998244353
print((dp[S] % 998244353))
