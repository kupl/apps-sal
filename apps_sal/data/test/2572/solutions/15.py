from bisect import *
from collections import *
from math import *
from heapq import *
from typing import List
from itertools import *
from operator import *
from functools import *
import sys
'''
@lru_cache(None)
def fact(x):
    if x<2:
        return 1
    return fact(x-1)*x

@lru_cache(None)
def per(i,j):
    return fact(i)//fact(i-j)

@lru_cache(None)
def com(i,j):
    return per(i,j)//fact(j)

def linc(f,t,l,r):
    while l<r:
        mid=(l+r)//2
        if t>f(mid):
            l=mid+1
        else:
            r=mid
    return l

def rinc(f,t,l,r):
    while l<r:
        mid=(l+r+1)//2
        if t<f(mid):
            r=mid-1
        else:
            l=mid
    return l

def ldec(f,t,l,r):
    while l<r:
        mid=(l+r)//2
        if t<f(mid):
            l=mid+1
        else:
            r=mid
    return l

def rdec(f,t,l,r):
    while l<r:
        mid=(l+r+1)//2
        if t>f(mid):
            r=mid-1
        else:
            l=mid
    return l

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def power2(n):
    while not n&1:
        n>>=1
    return n==1
'''
'''
import time
s=time.time()
e=time.time()
print(e-s)
'''

t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    used = set()
    ans = 0
    for i in range(n // 2 + 1):
        for j in range(m // 2 + 1):
            if (i, j) not in used:
                tmp = set([(i, j), (n - 1 - i, j), (n - 1 - i, m - 1 - j), (i, m - 1 - j)])
                used |= tmp
                if len(tmp) == 1:
                    continue
                elif len(tmp) == 2:
                    (x, y), (a, b) = tmp
                    ans += abs(arr[x][y] - arr[a][b])
                else:
                    res = []
                    for x, y in tmp:
                        res.append(arr[x][y])
                    res.sort()
                    ans += min(sum(abs(res[i] - res[j]) for j in range(4)) for i in range(1, 3))

    print(ans)
'''
n,m=map(int,input().split())
a=[]
b=[]
c=[]
d=[]
for i in range(n):
    ai,bi=map(int,input().split())
    a.append(ai)
    b.append(bi)
for i in range(m):
    ci,di=map(int,input().split())
    c.append(ci)
    d.append(di)
dic={}
for i in range(n):
    for j in range(m):
        x=c[j]-a[i]+1
        y=d[j]-b[i]+1
        if x>0 and y>0:
            if x in dic:
                dic[x]=min(dic[x],y)
            else:
                dic[x]=y
#print(dic)
if not dic:
    ans=0
else:
    res=sorted(dic.items())    
    n=len(res)
    ans=res[-1][0]
    ym=res[-1][1]
    for i in range(n-2,-1,-1):
        ans=min(ans,res[i][0]+ym)
        ym=max(ym,res[i][1])
    ans=min(ym,ans)
print(ans)
'''
