import numpy as N
n,k=map(int,input().split())
A=N.array(list(map(int,input().split())))
A.sort()
p=A[A>0]
z=N.count_nonzero(A==0)
m=A[A<0]
r=10**19
l=-r
while r-l>1:
    b=(l+r)//2
    c=0
    if b>=0:
        c+=z*n
    c+=A.searchsorted(b//p,side='right').sum()
    c+=n*len(m)-A.searchsorted(-(-b//m),side='left').sum()
    c-=N.count_nonzero(A*A<=b)
    if c//2>=k:
        r=b
    else:
        l=b
print(r)
