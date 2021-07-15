N, A = map(int, input().split())
X = list(map(int, input().split()))
sumX = 2501

dp = [[[0 for _ in range(sumX)] for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for j in range(N):
    for k in range(N):
        for s in range(sumX):
            if dp[j][k][s]==0:
                continue
            dp[j+1][k][s] += dp[j][k][s]
            dp[j+1][k+1][s+X[j]] += dp[j][k][s]
ans = 0

for i in range(N+1):
    ans += dp[N][i][i*A]
print(ans-1)
