(h, w, k) = map(int, input().split())
f = [1, 1, 2, 3, 5, 8, 13, 21]
m = 10 ** 9 + 7
dp = [[1] + [0] * (w - 1) for i in range(h + 1)]
h = 0 if w == 1 else h
for i in range(1, h + 1):
    for j in range(w):
        if j == 0:
            dp[i][0] = (dp[i - 1][0] * f[w - 1] + dp[i - 1][1] * f[w - 2]) % m
        elif j == w - 1:
            dp[i][w - 1] = (dp[i - 1][w - 1] * f[w - 1] + dp[i - 1][w - 2] * f[w - 2]) % m
        else:
            dp[i][j] = (dp[i - 1][j] * f[j] * f[w - j - 1] + dp[i - 1][j - 1] * f[j - 1] * f[w - j - 1] + dp[i - 1][j + 1] * f[j] * f[w - j - 2]) % m
print(dp[h][k - 1])
