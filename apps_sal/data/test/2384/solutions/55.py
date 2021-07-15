n = int(input())
A = list(map(int,input().split()))
dp = [[[0,0,0] for i in range(2)] for i in range(n+1)]
for i in range(1,n+1):
    if i%2 == 1:
        if i > 1:
            dp[i][0][1] = dp[i-1][1][0]+A[i-1]
            dp[i][0][2] = dp[i-1][1][1]+A[i-1]
            dp[i][1][0] = max(dp[i-1][0][0],dp[i-1][1][0])
            dp[i][1][1] = max(dp[i-1][0][1],dp[i-1][1][1])
        else:
            dp[i][0][2] = A[0]
    else:
        dp[i][0][0] = dp[i-1][1][0]+A[i-1]
        dp[i][0][1] = dp[i-1][1][1]+A[i-1]
        dp[i][1][0] = max(dp[i-1][0][1],dp[i-1][1][1])
        dp[i][1][1] = dp[i-1][0][2]
if n%2 == 0:
    print(max(dp[n][0][1],dp[n][1][1]))
else:
    print(max(dp[n][0][1],dp[n][1][1]))
