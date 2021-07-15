n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
a.sort()
import numpy as np
def bisearch(t):
  dp=np.full(k+1,False)
  dp[0]=True
  for i in range(n):
    if i==t:continue
    dp[a[i]:] = np.logical_or(dp[a[i]:], dp[:-a[i]]) 
  return any(dp[max(0,k-a[t]):k])
l,r=-1,n
while r-l>1:
  x=(l+r)//2
  if bisearch(x):
    r=x
  else:
    l=x
print(r)

