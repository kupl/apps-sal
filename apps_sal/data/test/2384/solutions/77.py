N = int(input())
A = list(map(int,input().split()))
odds_or_even = N%2+2
inf = -float("inf")
dp = [[inf for _ in range(N+1)] for _ in range(odds_or_even)]
dp[0][0] = 0
for i in range(N):
    dp[0][i+1] = dp[0][i]+A[i]*((i+1)%2)
for j in range(1,odds_or_even):
    for i in range(N):
        dp[j][i+1] = max(dp[j-1][i],dp[j][i]+A[i]*((i+j+1)%2))

print(dp[odds_or_even-1][N])
