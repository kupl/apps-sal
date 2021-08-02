N, A = map(int, input().split())
x = list(map(int, input().split()))
dp = [[[0] * (2501) for i in range(N + 1)] for k in range(N + 1)]
dp[0][0][0] = 1
for j in range(N):
    for k in range(N):
        for i in range(2501):
            if dp[j][k][i] == 0:
                continue
            dp[j + 1][k][i] += dp[j][k][i]
            dp[j + 1][k + 1][i + x[j]] += dp[j][k][i]
ans = 0
for j in range(N + 1):
    ans += dp[N][j][j * A]
print(ans - 1)
