import sys
input = sys.stdin.readline
t=int(input()) 
for rainbow in range(t):
    n=int(input())
    f=[tuple(map(int,input().split())) for i in range(n)]
    dp=[0]*n;dp1=[0]*n;dp2=[0]*n
    dp1[0]=f[0][1];dp2[0]=f[0][1]*2
    for i in range(1,n):
        a=f[i-1][0]
        b=f[i][0]
        if b==a:
            dp[i]=min(dp1[i-1],dp2[i-1])
            dp1[i]=f[i][1]+min(dp[i-1],dp2[i-1])
            dp2[i]=f[i][1]*2+min(dp[i-1],dp1[i-1])
        elif b==a+1:
            dp[i]=min(dp[i-1],dp2[i-1])
            dp1[i]=f[i][1]+min(dp[i-1],dp1[i-1])
            dp2[i]=f[i][1]*2+min(dp[i-1],dp1[i-1],dp2[i-1])
        elif b==a+2:
            dp[i]=min(dp[i-1],dp1[i-1])
            dp1[i]=f[i][1]+min(dp[i-1],dp1[i-1],dp2[i-1])
            dp2[i]=f[i][1]*2+min(dp[i-1],dp1[i-1],dp2[i-1])
        elif b==a-1:
            dp[i]=min(dp[i-1],dp1[i-1],dp2[i-1])
            dp1[i]=f[i][1]+min(dp1[i-1],dp2[i-1])
            dp2[i]=f[i][1]*2+min(dp[i-1],dp2[i-1])
        elif b==a-2:
            dp[i]=min(dp[i-1],dp1[i-1],dp2[i-1])
            dp1[i]=f[i][1]+min(dp[i-1],dp1[i-1],dp2[i-1])
            dp2[i]=f[i][1]*2+min(dp1[i-1],dp2[i-1])
        else:
            dp[i]=min(dp[i-1],dp1[i-1],dp2[i-1])
            dp1[i]=f[i][1]+min(dp[i-1],dp1[i-1],dp2[i-1])
            dp2[i]=f[i][1]*2+min(dp[i-1],dp1[i-1],dp2[i-1])
    print(min(dp[n-1],dp1[n-1],dp2[n-1]))
