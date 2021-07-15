n,c=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
dp=[[0]*2 for _ in range(n+1)]
dp[1][1]=c
for i in range(2,n+1):
    dp[i][0]=min(dp[i-1][0],dp[i-1][1])+l1[i-2]
    dp[i][1]=min(dp[i-1][0]+l2[i-2]+c,dp[i-1][1]+l2[i-2])
for i in range(1,n+1):
    print(min(dp[i]),end=" ")
    
