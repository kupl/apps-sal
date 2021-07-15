n,l,r=list(map(int,input().split()))
modz=r//3 - (l-1)//3
modo=(r+2)//3 - (l+1)//3
modt=(r+1)//3 - l//3
mod=1000000007
dp=[None]*(n+1)
for i in range(n+1):
    dp[i]=[0]*3
dp[1][0]=modz
dp[1][1]=modo
dp[1][2]=modt
for i in range(2,n+1):
        dp[i][0]=(dp[i-1][0]*modz + dp[i-1][1]*modt + dp[i-1][2]*modo)%mod
        dp[i][1]=(dp[i-1][0]*modo + dp[i-1][1]*modz + dp[i-1][2]*modt)%mod
        dp[i][2]=(dp[i-1][0]*modt + dp[i-1][1]*modo + dp[i-1][2]*modz)%mod
print(dp[n][0])
#print(dp)
#print(modz,modo,modt)

