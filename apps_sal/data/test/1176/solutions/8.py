N = int(input())
INF = float("inf")
A = list(map(int, input().split()))
# dp[i+1][j]: i番目まで見てj=0(i番目がそのまま),j=1(i番目が逆転)の時の最大値
dp = [[-INF] * 2 for _ in range(N)]
dp[0][0] = 0
dp[0][1] = 0
dp[1][0] = A[0] + A[1]
dp[1][1] = -(A[0] + A[1])
for i in range(2, N):
    dp[i][0] = max(dp[i - 1][0] + A[i], dp[i - 1][1] + A[i])
    dp[i][1] = max(dp[i - 1][0] - (A[i - 1] * 2 + A[i]), dp[i - 1][1] + A[i - 1] * 2 - A[i])
# print(dp)
ans = max(dp[N - 1])
print(ans)
