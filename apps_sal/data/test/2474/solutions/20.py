n=int(input())
lists=list(map(int,input().split()))
lists=sorted(lists,reverse=True)

mod=10**9+7
dp=[0 for i in range(n+1)]
dp[1]=2*lists[0]
for i in range(1,n):
    x=lists[i]
    y=pow(2,i,mod)
  
    dp[i+1]=4*dp[i]+(i+2)*(y**2)*lists[i]
    dp[i+1]%=mod

print(dp[n]%mod)
