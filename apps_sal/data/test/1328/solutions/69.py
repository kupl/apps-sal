n, ma, mb = list(map(int, input().split()))
r = [0] * n
c = [0] * n
for i in range(n):
    a, b, c[i] = list(map(int, input().split()))
    r[i] = a * mb - b * ma
dp = [[10 ** 9] * 4001 for i in range(n + 1)]
for i in range(n):
    for j in range(4001):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        if j == 2000:
            dp[i + 1][j + r[i]] = min(dp[i + 1][j + r[i]], c[i])
        if 0 <= j + r[i] <= 4000:
            dp[i + 1][j + r[i]] = min(dp[i + 1][j + r[i]], dp[i][j] + c[i])
if dp[n][2000] < 10 ** 9:
    print((dp[n][2000]))
else:
    print((-1))
