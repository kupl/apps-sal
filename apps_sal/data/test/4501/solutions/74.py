n, a = list(map(int, input().split()))
x = list(map(int, input().split()))
for i in range(n):
    x[i] -= a
# dp[i][j] = i番目までで(j-2500)を何個作れるか
dp = [[0] * 5001 for i in range(n)]
dp[0][x[0] + 2500] = 1
for i in range(1, n):
    dp[i][x[i] + 2500] = 1
    for j in range(5000):
        for k in range(2):
            if 0 <= j - k * x[i] <= 5000:
                dp[i][j] += dp[i - 1][j - k * x[i]]
print((dp[n - 1][2500]))
