n, a = list(map(int, input().split()))
x = list(map(int, input().split()))
for i in range(n):
    x[i] -= a
dp = [[0] * 5001 for i in range(n + 1)]
dp[0][2500] = 1
for i in range(n):
    for j in range(5000):
        for k in range(2):
            if 0 <= j - k * x[i] <= 5000:
                dp[i + 1][j] += dp[i][j - k * x[i]]
print((dp[n][2500] - 1))
