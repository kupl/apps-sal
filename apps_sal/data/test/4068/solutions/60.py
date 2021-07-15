n,m=map(int,input().split())
a=[int(input()) for i in range(m)]+[-1]
dp=[0]*(10**5+5)

dp[0],idx=1,0
  
for i in range(1,n+1):
  if a[idx]==i:
    idx+=1
    dp[i]=0
    if dp[i-1]==0: # continuous case
      print(0)
      return
  else:
    dp[i]+=dp[i-1]+dp[i-2]
    dp[i]%=(10**9+7)
    
print(dp[n])
