N = int(input())
dp = [[]for i in range(87)] 
dp[0] = 2
dp[1] = 1

for i in range(2,87):
    dp[i] = dp[i-1]+dp[i-2]
    if i == N:
        print(dp[i])
        break
else:
    print(dp[N])
