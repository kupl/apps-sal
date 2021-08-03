n, a, *l = map(int, open(0).read().split())
R = 2500
dp = [[0] * R * 2, [0] * R * 2]
dp[0][0] = 1
t = 0
for i in range(n):
    u = 1 - t
    for s in range(-R, R):
        dp[u][s] = dp[t][s] + dp[t][s - l[i] + a]
    t = u
print(dp[t][0] - 1)
