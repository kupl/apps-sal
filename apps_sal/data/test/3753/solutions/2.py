from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
import math
import time
ts=time.time()
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return list(map(int,input().split()))
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
mo=10**9+7
from math import log
input = sys.stdin.readline

pr=False
#pr=True
def tprint(*a):
    if pr:print(*a)
    return

n,m=MI()
mp=[[1]*(m+2)]
if m==1:
    for i in range(n):
        for j in list(input()):
            if j=='#':
                print(0)
                return
    print(1)
    return

for i in range(n):
    a=[1]
    for j in list(input()):
        if j=='#':
            a.append(1)
        else:
            a.append(0)
    mp.append(a+[1])
mp.append([1]*(m+2))

def search():
    go=[[0]*(m+2) for _ in range(n+2)]
    go[0][1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if mp[i][j]!=1:
                if go[i-1][j]+go[i][j-1]>0: go[i][j]=1
    go[0][1]=0
    return go

def bc_search(go):
    bc=[[0]*(m+2) for _ in range(n+2)]
    bc[n+1][m]=1
    for i in range(n,0,-1):
        for j in range(m,0,-1):
            if go[i][j]!=0:
                if bc[i+1][j]+bc[i][j+1]>0: bc[i][j]=1
    bc[n+1][m]=0
    return bc

go=search()
bc=bc_search(go)
G=[[0]*(m+3)]
G+=[[0]+[bc[i][j] for j in range(m+2)] for i in range(n+2)]

for i in range(n+2):
    for j in range(m+2):
        G[i+1][j+1]+=G[i+1][j]+G[i][j+1]-G[i][j]

if go[n][m]==0:
    ans=0
else:
    ans=2
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i*j==1 or i*j==n*m:
                continue
            s=0
            if j+1<m+3+10: s+=G[i][m+2]-G[i][j+1]
            if i+1<n+3+10: s+=G[n+2][j]-G[i+1][j]
            if s==0:
                ans=1
                tprint(i,j,G[i+1][j+1])

print(ans)

