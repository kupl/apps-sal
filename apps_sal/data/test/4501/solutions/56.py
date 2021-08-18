
NMAX = 55

N, A = list(map(int, input().split()))
X = list(map(int, input().split()))

dp = [[[0] * NMAX for s in range(3000)] for i in range(NMAX)]

dp[0][0][0] = 1
for i in range(N):
    for s in range(3000):
        for k in range(N + 1):
            if dp[i][s][k] == 0:
                continue
            dp[i + 1][s][k] += dp[i][s][k]
            dp[i + 1][s + X[i]][k + 1] += dp[i][s][k]

ans = 0
for k in range(1, N + 1):
    ans += dp[N][A * k][k]

print(ans)
