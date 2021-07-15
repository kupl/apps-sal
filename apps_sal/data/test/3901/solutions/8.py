from math import gcd
from functools import *
@lru_cache(maxsize=None)
def gcd1(a,b):
    return gcd(a,b)
def solve(k,n,a,g): 
    for i in range(n-k):
        g[i]=gcd1(g[i],a[i+k])
        if g[i]==1:
            return k
    return -1
def easy():
    n=int(input())
    a=[int(i) for i in input().split()]
    g=a[:]
    if n==1:
        if a[0]==1:
            print(0)
        else:
            print(-1)
    elif a.count(1)!=0:
        print(n-a.count(1))
    else:
        for i in range(n):
            cur=solve(i,n,a,g)
            if cur==i:
                print(n+cur-1)
                break
        else:
            print(-1)
easy()

