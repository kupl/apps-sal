import numpy as np

n, k = list(map(int, input().split()))
a = np.array(list(map(int, input().split())))

L = len(f'{10**12:b}')
dp = np.full((L+1, 2), -1, dtype=np.int64)
dp[0, 0] = 0
for i in range(L):
    d = 1 << (L-i-1)
    cnt = np.count_nonzero(a & d)
    val0 = d * cnt
    val1 = d * (n - cnt)

    if dp[i, 1] != -1:
        dp[i+1, 1] = max(dp[i+1, 1], dp[i, 1] + max(val0, val1))
    if dp[i, 0] != -1:
        if k & d:
            dp[i+1, 1] = max(dp[i+1, 1], dp[i, 0] + val0)
    if dp[i, 0] != -1:
        if k & d:
            dp[i+1, 0] = max(dp[i+1, 0], dp[i, 0] + val1)
        else:
            dp[i+1, 0] = max(dp[i+1, 0], dp[i, 0] + val0)

print((max(dp[L, 0], dp[L, 1])))

