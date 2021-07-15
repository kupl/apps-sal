n=int(input())
a=[int(i) for i in input().split()]
from math import gcd
g=a[:]
def solve(k):
    for i in range(n-k):
        g[i]=gcd(g[i],a[i+k])
        if g[i]==1:
            return k
    return -1
if n==1:
    if a[0]==1:
        print(0)
    else:
        print(-1)
elif a.count(1)!=0:
    print(n-a.count(1))
else:
    for i in range(n):
        cur=solve(i)
        if cur==i:
            print(n+cur-1)
            break
    else:
        print(-1)

