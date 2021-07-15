from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from bisect import bisect_right
from itertools import accumulate

n,m,k=nii()
a=lnii()
b=lnii()
ar=[0]+list(accumulate(a))
br=list(accumulate(b))

ans=0
for i in range(n+1):
  time=ar[i]
  if time>k:
    break
  t_ans=i
  inx=bisect_right(br,k-time)
  t_ans+=inx
  ans=max(ans,t_ans)
print(ans)
