import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return list(map(int,input().split()))
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

n,m = I()
a = []
b = []

for _ in range(n):
    a += [list(input())]
for _ in range(m):
    b += [list(input())]

for i in range(n-m+1):
    for j in range(n-m+1):
        if [k[j:m+j] for k in a[i:m+i]] == b:
            print('Yes')
            return
print('No')

