import numpy as np
n,k=map(int,input().split())
a=np.array(list(map(int,input().split())))
a.sort()
p=a[a>0]
z=a[a==0]
m=a[a<0]
l=-10**18
r=10**18
while r-l>1:
  mid=(r+l)//2
  cnt=0
  if mid>=0:
    cnt+=len(z)*n
  cnt+=a.searchsorted(mid//p,side='right').sum()
  cnt+=(n-a.searchsorted(-(-mid//m),side='left')).sum()
  cnt-=np.count_nonzero(a*a<=mid)
  cnt//=2
  if cnt>=k:
    r=mid
  else:
    l=mid
print(r)
