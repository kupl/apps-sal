(N, A) = map(int, input().split())
X = list(map(int, input().split()))
dp = [[[0] * 6000 for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
for i in range(N):
    for j in range(N):
        for k in range(5000):
            if dp[i][j][k] == 0:
                continue
            dp[i + 1][j][k] += dp[i][j][k]
            dp[i + 1][j + 1][k + X[i]] += dp[i][j][k]
C = 0
for i in range(N + 1):
    C += dp[N][i][i * A]
print(C - 1)
