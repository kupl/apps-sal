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
for i in range(t):
    #n,m=map(int,input().split())
    n,m=1,0
    graph=defaultdict(set)
    for i in range(m):
        u,v=map(int,input().split())
        graph[u-1].add(v-1)
    visited=[0]*n
    ans=[]
    def delchild(u):
        for child in graph[u]:
            visited[child]=1
            ans.append(child+1)
    for i in range(n):
        if not visited[i]:
            children=graph[i]
            if len(children)==1:
                u=children.pop()
                visited[u]=1
                delchild(u)
            elif len(children)==2:
                u=children.pop()
                v=children.pop()
                if u in graph[v]:
                    delchild(v)
                    visited[v]=1
                elif v in graph[u]:
                    delchild(u)
                    visited[u]=1
                else:
                    delchild(u)
                    delchild(v)
                    visited[u]=visited[v]=1
    print(len(ans))
    sys.stdout.flush()
    print(' '.join(map(str,ans)))
    sys.stdout.flush()

import time
s=time.time()
e=time.time()
print(e-s)
'''
'''
t=int(input())
for i in range(t):
    #n,m=map(int,input().split())
    n=int(input())
    x=int(sqrt(n))
    if x*x==n:
        ans=2*x-2
    elif x*(x+1)>=n:
        ans=2*x-1
    else:
        ans=2*x
    print(ans)
'''
n=int(input())
arr=list(map(int,input().split()))
d={0}
pre=0
ans=0
for a in arr:
    pre+=a
    if pre in d:
        ans+=1
        pre=a
        d={0,a}
    else:
        d.add(pre)
print(ans)
                
    


