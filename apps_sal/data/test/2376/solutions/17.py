import numpy as np
n, W = list(map(int, input().split()))
wv = [list(map(int, input().split()))]
w0 = wv[0][0] - 1
wv[0][0] = 1
for _ in range(n - 1):
    w, v = list(map(int, input().split()))
    wv.append([w - w0, v])
dp = np.full((n + 1, 401), 0, int)
dp[0] = 0
for w, v in wv:
    for i in range(n):
        dp[n - i][w:] = np.maximum(dp[n - i][w:], dp[n - i - 1][:-w] + v)
ans = 0
for i in range(1, n + 1):
    if W - i * w0 <= 0:
        break
    ans = max(ans, dp[i][min(W - i * w0, 400)])
print(ans)
