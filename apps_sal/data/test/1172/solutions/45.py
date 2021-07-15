mod=10**9+7
s=list(input())
s=['-']+s
l=len(s)
dp=[[0 for j in range(4)] for i in range(l)]
dp[0][0]=1
for i in range(1,l):
    for j in range(4):
        dp[i][j]=dp[i-1][j]
        if s[i]=='?':
            dp[i][j]*=3;
        if j and (s[i]=='?' or 'ABC'[j-1]==s[i]):
            dp[i][j]+=dp[i-1][j-1]
        dp[i][j]%=mod
print(dp[-1][3])
