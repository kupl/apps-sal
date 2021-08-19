import numpy as np
(N, T) = map(int, input().split())
item = [None] * N
for i in range(N):
    (w, v) = map(int, input().split())
    item[i] = [w, v]
item.sort(key=lambda x: x[0])
dp = np.zeros(T, dtype=int)
ans = 0
for i in range(N):
    (w, v) = item[i]
    ans = max(ans, dp.max() + v)
    dp[w:] = np.maximum(dp[w:], dp[:-w] + v)
print(ans)
