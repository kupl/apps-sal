import numpy as np
n = int(input())
a = list(map(int,input().split()))
dp = np.full((2, n//2 + 1), -10**18, dtype=np.int64)
"""
dp[i][j] := iは偶奇, jは何個決めるか
"""
dp[0][0] = 0
dp[1][0] = 0
for i in range(n):
	k = i % 2
	for j in [2, 1, 0]:
		if i//2+j <= n//2:
			if i//2-1+j >= 0:
				dp[k][i//2+j] = np.maximum(dp[1-k][i//2+j], dp[k][i//2-1+j]+a[i])

print(max(dp[0][n//2], dp[1][n//2]))
