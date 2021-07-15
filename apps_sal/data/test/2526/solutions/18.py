import sys, bisect, math, itertools, string, queue, copy
import numpy as np
import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

x,y,a,b,c = inpm()
p = list(reversed(sorted(inpl())))
q = list(reversed(sorted(inpl())))
r = list(reversed(sorted(inpl())))
pp = x-1
qq = y-1
rr = 0

tmp = []
tmp.extend(p[:pp+1])
tmp.extend(q[:qq+1])
tmp.extend(r)

tmp = list(reversed(sorted(tmp)))
ans = sum(tmp[:x+y])
print(ans)
