s=input()
mod=pow(10,9)+7
dp=[0]*4
dp[0]=1
for si in s:
  if si=='A':
    dp[1]+=dp[0]
  elif si=='B':
    dp[2]+=dp[1]
  elif si=='C':
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
  dp[3]%=mod
  dp[2]%=mod
  dp[1]%=mod
  dp[0]%=mod
print((dp[3]))

