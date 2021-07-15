S=input()
ans,n=0,len(S)
dp=[0]*(2019)
s,dp[0],k=0,1,1
for i in S[::-1]:
  s=(s+int(i)*k)%2019
  k=(k*10)%2019
  ans+=dp[s]
  dp[s]+=1
print(ans)
