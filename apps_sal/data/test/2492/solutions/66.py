import numpy as np
 
N,K=list(map(int, input().split()))
A=np.sort(np.array(input().split(),np.int64))
z=A[A==0]
p=A[A>0]
n=A[A<0]
 
def f(x):
 cnt=0
 if x>=0:
  cnt+=len(z)*N
 cnt+=np.searchsorted(A,x//p,side='right').sum()
 cnt+=(N-np.searchsorted(A,(-x-1)//(-n),side='right')).sum()
 cnt-=np.count_nonzero(A*A<=x)
 assert cnt%2==0
 return cnt//2
 
l=-10**18
r=10**18
while l+1<r:
 x=(l+r)//2
 if f(x)>=K:
  r=x
 else:
  l=x
print(r)

