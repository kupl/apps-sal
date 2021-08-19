import numpy as np
(n, a) = list(map(int, input().split()))
x = list(map(int, input().split()))
dp = np.zeros((n + 1, 2501), int)
dp[0, 0] = 1
for xi in x:
    for i in range(n - 1, -1, -1):
        dp[i + 1][xi:] += dp[i, :-xi]
ans = 0
for i in range(1, n + 1):
    ans += dp[i, i * a]
print(ans)
