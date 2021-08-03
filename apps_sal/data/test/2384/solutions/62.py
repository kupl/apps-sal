N = int(input())
A = [int(x) for x in input().split()]

dp = [[0] * 3] * N

dp[0][0] = 0  # ((i+1)-1)/2
dp[0][1] = 0  # (i+1)/2
dp[0][2] = A[0]  # ((i+1)+1)/2

for i in range(1, N):

    if i % 2 == 0:
        dp[i][0] = dp[i - 1][0] + A[i]
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][2])
        dp[i][2] = dp[i - 1][2] + A[i]
    else:
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][1] + A[i]
        dp[i][2] = dp[i - 1][2]

if N % 2 == 0:
    print(max(dp[N - 1][1], dp[N - 1][2]))
else:
    print(max(dp[N - 1][0], dp[N - 1][1]))
