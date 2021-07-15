n=int(input())

a=[1,6,36,216,1296,7776,46656,9,81,729,6561,59049]

inf=float('inf')
dp=[inf for _ in range(100000+1)]
dp[0]=0
dp[1]=1

for x in range(1,100001):
  for b in a:
    if b<=x:
      dp[x]=min(dp[x],dp[x-b]+1)
      
print((dp[n]))

