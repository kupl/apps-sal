import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
from functools import reduce
def s(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return list(map(int,input().split()))
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
def gcd(*numbers): reduce(math.gcd, numbers)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0

A, B, Q = I()
inf = float("inf")
s = [-inf]+sorted([k() for _ in range(A)])+[inf]
t = [-inf]+sorted([k() for _ in range(B)])+[inf]
aa = []

for i in range(Q):
    q = k()
    S = bisect.bisect(s,q)
    T = bisect.bisect(t,q)
    ans = inf
    for j in [s[S-1],s[S]]:
        for z in [t[T-1],t[T]]:
            x = abs(j-q)+abs(j-z)
            y = abs(z-q)+abs(j-z)
            ans = min(ans,x,y)
    aa.append(ans)

for i in aa:
    print(i)

