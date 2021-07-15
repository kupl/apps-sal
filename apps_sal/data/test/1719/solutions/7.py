N=int(input())
MOD=10**9+7
dp=[[[[0]*5 for _ in range(5)] for _ in range(5)]for _ in range(N+1)]
ans=0
dp[0][0][0][0]=1
for n in range(N):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(1,5):
                    if j==1 and k==2 and l==3:continue
                    if j==1 and k==3 and l==2:continue
                    if j==3 and k==1 and l==2:continue
                    if i==1 and j==3 and l==2:continue
                    if i==1 and k==3 and l==2:continue
                    dp[n+1][j][k][l]+=dp[n][i][j][k]
for j in range(1,5):
    for k in range(1,5):
        for l in range(1,5):
            ans+=dp[N][j][k][l]
print(ans%MOD)
