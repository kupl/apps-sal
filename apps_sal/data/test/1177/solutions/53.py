import numpy as np
from sys import stdin
(N, S) = list(map(int, stdin.readline().split()))
A = list(map(int, stdin.readline().split()))
M = 998244353
V = max(max(A), S)
ans = 0
cs = np.zeros(V + 1, dtype=np.int64)
for (i, a) in enumerate(A):
    dp = np.zeros(V + 1, dtype=np.int64)
    dp[a] = i + 1
    dp[a + 1:S + 1] = cs[np.arange(a + 1, S + 1) - a]
    cs = (cs + dp) % M
    ans = (ans + (N - i) * dp[S]) % M
print(ans)
