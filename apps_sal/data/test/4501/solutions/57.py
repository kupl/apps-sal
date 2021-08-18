import numpy as np
n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = np.zeros((n + 1, n + 1, 3001)).astype(np.int64)
dp[0][0][0] = 1

for i in range(n):
    _x = x[i]
    for j in range(n):
        dp[i + 1, j + 1, _x:] += dp[i, j, :-_x]
        dp[i + 1, j, :] += dp[i, j, :]

ans = 0
for j in range(1, n + 1):
    ans += dp[n, j, j * a]
print(ans)
