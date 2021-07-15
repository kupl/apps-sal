n=int(input())
s=list(map(int,input().split()))
mod=998244353
cm=[[0 for i in range(n+2)]for j in range(n+2)]
for i in range(n+2):
    cm[i][0]=1
for i in range(1,n+2):
    for j in range(1,n+2):
        cm[i][j]=cm[i-1][j]+cm[i-1][j-1]
        cm[i][j]=cm[i][j]%mod
dp=[0 for i in range(n+2)]
acum=[0 for i in range(n+2)]
for i in range(n-1,-1,-1):
    acum[i]=acum[i+1]
    if s[i]<=0:
        continue
    for j in range(i+s[i],n):
        dp[i]=(cm[j-(s[i]+i)+s[i]-1][s[i]-1]+cm[j-(s[i]+i)+s[i]-1][s[i]-1]*acum[j+1]+dp[i])%mod
    acum[i]=(dp[i]+acum[i])%mod
print(acum[0])

