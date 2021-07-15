n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[0,2,5,5,4,5,6,3,7,6]
wv=[]
for i in a:
  wv.append((b[i],i))
wv.sort()
dp=[-1 for i in range(n+1)]
dp[0]=0
for i in range(1,n+1):
  for w,v in wv:
    if i-w<0:
      continue
    if dp[i-w]==-1:
      continue
    dp[i]=max(dp[i],dp[i-w]*10+v)
print(dp[n])
