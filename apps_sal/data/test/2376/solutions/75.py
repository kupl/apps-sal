n, W = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(n)]

dp = [[[-1] * (3 * n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0
w1 = wv[0][0]

for i, (w, v) in enumerate(wv):
    for j in range(i + 1):
        for k in range(3 * n + 1):
            if dp[i][j][k] != -1:
                dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])
                w_diff = w - w1
                if j + 1 <= n and k + w_diff <= 3 * n:
                    dp[i+1][j+1][k+w_diff] = max(dp[i+1][j+1][k+w_diff], dp[i][j][k] + v)

ans = 0
for j in range(n + 1):
    w_diff_mx = min(W - w1 * j, 3 * n)
    for k in range(w_diff_mx + 1):
        ans = max(ans, dp[n][j][k])

print(ans)

