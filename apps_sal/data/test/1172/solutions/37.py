S=input()
MOD=pow(10,9)+7
dp=[0]*4
dp[0]=1
for s in S:
  if s=='A':
    dp[1]+=dp[0]
  elif s=='B':
    dp[2]+=dp[1]
  elif s=='C':
    dp[3]+=dp[2]
  else:
    tmp3=dp[2]
    tmp2=dp[1]
    tmp1=dp[0]
    dp[3]*=3
    dp[3]+=tmp3
    dp[2]*=3
    dp[2]+=tmp2
    dp[1]*=3
    dp[1]+=tmp1
    dp[0]*=3
  dp[3]%=MOD
  dp[2]%=MOD
  dp[1]%=MOD
  dp[0]%=MOD
print(dp[3])
