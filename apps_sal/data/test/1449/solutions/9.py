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

t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    #n=int(input())
    a=set(map(int,input().split()))
    n=len(a)
    if n==1:
        ans=1
    else:
        if k==1:
            ans=-1
        else:
            ans=ceil((n-1)/(k-1))
    print(ans)
'''
n,m=map(int,input().split())
graph=defaultdict(dict)
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u][v]=w
    graph[v][u]=w
def dij(u,v):
    graph[u][v]*=2
    graph[v][u]*=2
    d={}
    d[1]=0
    for i in range(2,n+1):
        d[i]=inf
    remain=set(range(2,n+1))
    for i in graph[1]:
        d[i]=graph[1][i]
    while remain:
        k=min(remain,key=lambda x: d[x])
        remain.remove(k)
        for i in remain:
            if i in graph[k]:
                d[i]=min(d[i],d[k]+graph[k][i])
    graph[u][v]//=2
    graph[v][u]//=2
    return d[n]
D={}
D[1]=0
for i in range(2,n+1):
    D[i]=inf
remain=set(range(2,n+1))
pre=[-1]*(n+1)
for i in graph[1]:
    D[i]=graph[1][i]
    pre[i]=1
while remain:
    k=min(remain,key=lambda x: D[x])
    remain.remove(k)
    for i in remain:
        if i in graph[k]:
            if D[i]>D[k]+graph[k][i]:
                D[i]=D[k]+graph[k][i]
                pre[i]=k
cur=ans=D[n]
node=n
while pre[node]!=-1:
    ans=max(ans,dij(node,pre[node]))
    node=pre[node]
print(ans-cur)
            
'''
    


