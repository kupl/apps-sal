n,m=map(int,input().split())
dp=[10**20]*(1<<n)
dp[0]=0
for i in range(m):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    bit=0
    for j in c:bit|=1<<(j-1)
    for j in range(1<<n):
        dp[j|bit]=min(dp[j|bit],dp[j]+a)
if dp[-1]==10**20:print(-1)
else:print(dp[-1])
