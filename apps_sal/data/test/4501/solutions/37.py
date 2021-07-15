n,a=list(map(int,input().split()))
x=list(map(int,input().split()))

for i in range(n):
    x[i]=x[i]-a
    
nx=n*n
dp=[[0]*(2*nx+1) for i in range(n+1)]

#print(dp)

dp[0][nx]=1

for j in range(1,n+1):
    jj=j-1
    for t in range(2*nx+1):
        if t-x[jj]<0 or 2*nx<t-x[jj]:
            dp[j][t]=dp[j-1][t]
        elif 0<t-x[jj] and  t-x[jj]<2*nx:
            dp[j][t]=dp[j-1][t]+dp[j-1][t-x[jj]]
        else:
            dp[j][t]=0

print((dp[n][nx]-1))
        

