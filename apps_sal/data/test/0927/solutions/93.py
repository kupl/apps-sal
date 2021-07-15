n,m=map(int, input().split())
lst=list(map(int,input().split()))
weight=[0,2,5,5,4,5,6,3,7,6]
DP=[-1]*(n+1)
DP[0]=0
for i in range(n+1):
  for x in lst:
    if i+weight[x]<n+1:
      DP[i+weight[x]]=max(DP[i+weight[x]], DP[i]*10+x)
print(DP[n])
