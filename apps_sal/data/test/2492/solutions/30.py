import numpy as np

def check(mid):
  cnt=0
  if mid>=0:
    cnt+=len(zero)*N
  cnt+=np.searchsorted(A, mid//pos, side="right").sum()
  cnt+=(N-np.searchsorted(A, (-mid-1)//(-neg), side="right")).sum()
  cnt-=np.count_nonzero(A*A<=mid)
  return cnt//2

N,K=map(int,input().split())
A=np.array(sorted(map(int,input().split())))

pos=A[A>0]
zero=A[A==0]
neg=A[A<0]

high=10**18
low=-10**18
while low+1<high:
  mid=(high+low)//2
  if check(mid)>=K:
    high=mid
  else:
    low=mid
print(high)
