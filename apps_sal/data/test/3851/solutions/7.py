def gcd(a,b):
    while b!=0:
        t=int(a)
        a=int(b)
        b=t%a
    return int(a)
from sys import stdin
n,k=list(map(int,stdin.readline().strip().split()))
a,b=list(map(int,stdin.readline().strip().split()))
mx=-10**20
mn=-mx
for i in range(n):
    nk=(k*i)

    l1=(-a)%(n*k)
    l2=(nk-b)%(n*k)
    l=0
    
    if l2>l1:
        l=l2-l1
    elif l2<l1:
        l=n*k-l1+l2
    if l==0:
        l=n*k
    if True:

        mn=min(mn,n*k/gcd(n*k,l))
        mx=max(mx,n*k/gcd(n*k,l))
    l1=(a)%(n*k)
    l2=(nk+b)%(n*k)
    l=0
    if l2>l1:
        l=l2-l1
    elif l2<l1:
        l=n*k-l1+l2
    if l==0:
        l=n*k
    if True:

        mn=min(mn,n*k/gcd(n*k,l))
        mx=max(mx,n*k/gcd(n*k,l))

    l1=(-a)%(n*k)
    l2=(nk+b)%(n*k)
    l=0
    if l2>l1:
        l=l2-l1
    elif l2<l1:
        l=n*k-l1+l2
    if l==0:
        l=n*k
    if True:

        mn=min(mn,n*k/gcd(n*k,l))
        mx=max(mx,n*k/gcd(n*k,l))

    l1=(a)%(n*k)
    l2=(nk-b)%(n*k)
    l=0
    if l2>l1:
        l=l2-l1
    elif l2<l1:
        l=n*k-l1+l2
    if l==0:
        l=n*k
    if True:

        mn=min(mn,n*k/gcd(n*k,l))
        mx=max(mx,n*k/gcd(n*k,l))
    
print(int(mn),int(mx))



