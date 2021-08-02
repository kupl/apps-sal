import numpy as np
n, t = list(map(int, input().split()))
item = [None] * n
ans = 0
dp = np.zeros(t, dtype=int)

for i in range(n):
    a, b = list(map(int, input().split()))
    item[i] = [a, b]
item.sort(key=lambda x: x[0])

for i in range(n):
    a, b = item[i]
    ans = max(ans, dp.max() + b)
    dp[a:] = np.maximum(dp[a:], dp[:-a] + b)

print(ans)
