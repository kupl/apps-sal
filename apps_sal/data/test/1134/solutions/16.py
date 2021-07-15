n=int(input())
mi=list(map(int,input().split()))
dp=[0]*n
dp[0]=1
ans=0
for i in range(1,n):
    dp[i]=max(dp[i-1],mi[i]+1)
for i in range(n-2,-1,-1):
    dp[i] = max(dp[i],dp[i+1]-1)
for i in range(n):
    ans+=dp[i]-mi[i]-1
print(ans)
