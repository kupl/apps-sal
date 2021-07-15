import numpy as np
n,k=map(int,input().split())
a=np.sort(np.array(input().split(),'int64'))

plus=a[a>0]
zeros=np.sum(a==0)
minus=a[a<0]

def counter(T):
  c=0
  if T>=0:
    c+=zeros*n
  c+=np.searchsorted(a,T//plus,side='right').sum()
  c+=(n-np.searchsorted(a,(-T-1)//(-minus),side='right')).sum()
  c-=np.count_nonzero(a*a<=T)
  return c//2

left=-10**18
right=10**18
while abs(right-left)>1:
  mid=(left+right)//2
  if counter(mid)>=k:
    right=mid
  else:
    left=mid
print(right)
