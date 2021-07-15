n, W = map(int, input().split())
wv = []
for i in range(n):
    wv.append(list(map(int, input().split())))
num = wv[0][0]
dp = [[-float("inf") for i in range(3 * (n - 1) + 1)] for j in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    w, v = wv[i][0], wv[i][1]
    w -= num
    for j in range(n - 1, -1, -1):
        for k in range(3 * (n - 1) + 1 - w):
            dp[j + 1][k + w] = max(dp[j + 1][k + w], dp[j][k] + v)
ans = 0
for i in range(3 * (n - 1) + 1):
    for j in range(n + 1):
        if j * num + i <= W:
            ans = max(ans, dp[j][i])
print(ans)
