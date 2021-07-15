n = int(input())
a = list(map(int,input().split()))
 
dp = [[0]*2 for _ in range(n+1)]
dp[1] = [0,a[0]]
dp[2] = [0,max(a[0],a[1])]
for i in range(3,n+1):
    if i%2 == 0:
        dp[i][0] = max(dp[i-1][0],dp[i-2][0]+a[i-1])
        dp[i][1] = max(dp[i-1][1],dp[i-2][1]+a[i-1])
    else:
        dp[i][0] = max(dp[i-1][1],dp[i-2][0]+a[i-1])
        dp[i][1] = dp[i-2][1]+a[i-1]
        
if n%2 == 0:
    print(dp[n][1])
else:
    print(dp[n][0])
