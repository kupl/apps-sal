n=int(input())
dp=[0]*(n+1)
for i in range(n+1):
  t=i
  count=0
  while t>0:
    count+=t%6
    t//=6
  t=n-i
  while t>0:
    count+=t%9
    t//=9
  dp[i]=count
print(min(dp))
