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
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N = i()
A = [0]+l()+[0]
d = []
for i in range(N+1):
    d.append(abs(A[i+1]-A[i]))
ans = sum(d)
for i in range(N):
    print(ans+abs(A[i]-A[i+2])-d[i]-d[i+1])
