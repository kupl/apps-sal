import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return list(map(int,input().split()))
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N,M = I()
links = [[] for _ in range(N)]
for i in range(M):
    x,y,z = I()
    links[x-1].append(y-1)
    links[y-1].append(x-1)
ans = 0
visited = [0]*N
def dfs(n):
    if visited[n]:
        return
    visited[n] = 1
    for l in links[n]:
        dfs(l)
for i in range(N):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)

