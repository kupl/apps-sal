import sys, math, random, re, heapq
from itertools import combinations as c, permutations as perm, product as p
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**9)
INF = float('inf')
#MOD = 10**9 + 7
MOD = 998244353
F = 1e-9


def si(): return input()
def ii(): return int(input())
def fi(): return float(input())
def lstr(): return input().split()
def lint(): return list(map(int, input().split()))
def lintdec(): return list(map(lambda x:int(x) - 1, input().split()))
def lnstr(n): return [input() for _ in range(n)]
def lnint(n): return [ii() for _ in range(n)]
def lint_list(n): return [lint() for _ in range(n)]
def lcm(a, b): return a * b // math.gcd(a, b)



#######################################################
n = int(input())

l = 1
r = n + 1
while r - l > 1:
    mid = (l + r) // 2
    s = mid * (mid + 1) // 2
    if s <= n + 1:
        l = mid
    elif s > n + 1:
        r = mid

print(n - l + 1)
