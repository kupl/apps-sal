MOD=10**9+7
S=input()
N=len(S)

dp=[[0]*4 for i in range(N+1)]

dp[0][0]=1

for i in range(N):
    dp[i+1][0]=dp[i][0] if (S[i]!='?') else dp[i][0]*3%MOD
    dp[i+1][1]=dp[i][1] if (S[i]!='A' and S[i]!='?') else (dp[i][1]+dp[i][0])%MOD if (S[i]=='A') else (dp[i][0]+dp[i][1]*3)%MOD
    dp[i+1][2]=dp[i][2] if (S[i]!='B' and S[i]!='?') else (dp[i][2]+dp[i][1])%MOD if (S[i]=='B') else (dp[i][1]+dp[i][2]*3)%MOD
    dp[i+1][3]=dp[i][3] if (S[i]!='C' and S[i]!='?') else (dp[i][3]+dp[i][2])%MOD if (S[i]=='C') else (dp[i][2]+dp[i][3]*3)%MOD

print(dp[N][3])
