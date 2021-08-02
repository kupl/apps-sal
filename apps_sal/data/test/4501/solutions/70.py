n, a, *l = map(int, open(0).read().split())
R = 2500
dp = [[0] * R * 2, [0] * R * 2]
dp[0][0] = 1
for i in range(n):
    for s in range(-R, R):
        dp[i + 1 & 1][s] = dp[i & 1][s] + dp[i & 1][s - l[i] + a]
print(dp[n & 1][0] - 1)
