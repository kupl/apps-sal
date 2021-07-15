h,n=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
mx=max(a for a,b in ab)
dp=[10**10]*(h+1+mx)
dp[0]=0
for i in range(1,h+1+mx):
  dp[i]=min(dp[i-a]+b for a,b in ab)
print(min(dp[h:]))
