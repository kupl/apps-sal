s=input()
n=len(s)
mod=10**9+7
dp=[[0]*2 for i in range(n+5)]
# dp[i][j]
#  : 右からi桁目までチェックしたときに
#     j=0:Lと一致している
#     j=1:L未満であることが確定している

dp[0][0]=1
for i in range(n):
  # i桁目がa+b=0のケース（つまりi桁目はa=b=0）
  if s[i]=='0':
    dp[i+1][0]=dp[i][0]
    dp[i+1][1]=dp[i][1]
  else:
    dp[i+1][1]=(dp[i][1]+dp[i][0])%mod
    
  # i桁目がa+b=1のケース（つまりi桁目はa=0,b=1 or a=1,b=0）
  if s[i]=='0':
    dp[i+1][1]+=dp[i][1]*2
    dp[i+1][1]%=mod
  else:
    dp[i+1][0]+=dp[i][0]*2
    dp[i+1][0]%=mod
    dp[i+1][1]+=dp[i][1]*2
    dp[i+1][1]%=mod
  
print((dp[n][0]+dp[n][1])%mod)
