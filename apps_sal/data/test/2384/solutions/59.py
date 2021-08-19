N = int(input())
A = list(map(int, input().split()))
k = 1 + N % 2
INF = 10 ** 18
dp = [[-INF for _ in range(4)] for _ in range(202020)]
dp[0][0] = 0
for i in range(N):
    for j in range(k + 1):
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
        now = dp[i][j]
        if (i + j) % 2 == 0:
            now += A[i]
        dp[i + 1][j] = max(dp[i + 1][j], now)
print(dp[N][k])
