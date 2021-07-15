p=10**9+7
import math
def prod(l):
    x=1
    for m in l:
        x*=m
    return x
n=int(input())
a=[]
k=int(math.log2(n))
x=n
while x>0:
    y=x//2
    a.append(x-y)
    x=y
c=[sum(a[i:]) for i in range(k+1)]
b=[n//(3*2**i)-n//(6*2**i) for i in range(k+1)]
d=[n//2**i-n//(3*2**i) for i in range(k+1)]
facs=[1]*(n+1)
for i in range(2,n+1):
    facs[i]=(i*facs[i-1])%p
start=k if n<3*(2**(k-1)) else 0
tot=0
for j in range(start,k+1):
    e=[a[i] for i in range(j)]+[d[j]]+[b[i] for i in range(j,k)]
    x=(facs[n]*prod(e))%p
    f=prod([sum(e[:i+1]) for i in range(k+1)])
    while f>1:
        x*=p//f+1
        f=(f*(p//f+1))%p
    tot+=x%p
print(tot%p)
