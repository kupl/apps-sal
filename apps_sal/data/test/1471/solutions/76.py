#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from math import gcd
from operator import add, itemgetter, mul, xor
def cmb(n,r,mod):
  bunshi=1
  bunbo=1
  for i in range(r):
    bunbo = bunbo*(i+1)%mod
    bunshi = bunshi*(n-i)%mod
  return (bunshi*pow(bunbo,mod-2,mod))%mod
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return list(map(int,input().split()))
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n = I()
graph =[[]*(n+1) for i in range(n+1)]
ans = [0]*(n+1)
for i in range(n-1):
    u,v,w = list(map(int,input().split()))
    w = w%2
    graph[u].append([v,w])
    graph[v].append([u,w])
#vをcに塗る。pはvの親
def dfs(v,p,c,ans):
    ans[v] = c
    for i in graph[v]:
        if i[0] == p:
            continue
        if i[1] == 1:
            dfs(i[0],v,1-c,ans)
        if i[1] == 0:
            dfs(i[0],v,c,ans)
dfs(1,0,0,ans)
for i in ans[1:]:
    print(i)

