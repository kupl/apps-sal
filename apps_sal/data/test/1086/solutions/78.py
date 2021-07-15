H,W=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
for i in range(H):
    B=list(map(int,input().split()))
    for j in range(W):
        A[i][j]=abs(A[i][j]-B[j])
D=80*(H+W)+1
D2=D*2
dp=[[0]*W for i in range(H)]
dp[0][0]|=1<<(D+A[0][0])
dp[0][0]|=1<<(D-A[0][0])
for i in range(H):
    for j in range(W):
        if i:
            dp[i][j]|=dp[i-1][j]<<A[i][j]
            dp[i][j]|=dp[i-1][j]>>A[i][j]
        if j:
            dp[i][j]|=dp[i][j-1]<<A[i][j]
            dp[i][j]|=dp[i][j-1]>>A[i][j]
res=dp[-1][-1]
ans=10**18
for i in range(D2):
    if res>>i&1:
        ans=min(ans,abs(D-i))
print(ans)
