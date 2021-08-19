import sys
import bisect
import math
import itertools
import string
import queue
import copy
import numpy as np
import scipy
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
def inp(): return int(input())
def inpm(): return map(int, input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])


n = inp()
ans = 0
n_ketasuu = len(str(n))
sta_max = int(str(n)[0])
end_max = int(str(n)[n_ketasuu - 1])
for i in range(1, n + 1):
    sta = int(str(i)[len(str(i)) - 1])
    end = int(str(i)[0])
    if sta == 0:
        continue
    # 1桁
    if sta == end:
        ans += 1
    # 2桁
    if n_ketasuu >= 2 and sta * 10 + end <= n:
        ans += 1
    # 3桁
    if n_ketasuu > 3 or (n_ketasuu == 3 and sta < sta_max):
        ans += 10
    elif n_ketasuu == 3 and sta == sta_max:
        ans += int(str(n)[1:n_ketasuu - 1])
        if end <= end_max:
            ans += 1
    # 4桁
    if n_ketasuu > 4 or (n_ketasuu == 4 and sta < sta_max):
        ans += 100
    elif n_ketasuu == 4 and sta == sta_max:
        ans += int(str(n)[1:n_ketasuu - 1])
        if end <= end_max:
            ans += 1
    # 5桁
    if n_ketasuu > 5 or (n_ketasuu == 5 and sta < sta_max):
        ans += 1000
    elif n_ketasuu == 5 and sta == sta_max:
        ans += int(str(n)[1:n_ketasuu - 1])
        if end <= end_max:
            ans += 1
    # 6桁
    if n_ketasuu > 6 or (n_ketasuu == 6 and sta < sta_max):
        ans += 10000
    elif n_ketasuu == 6 and sta == sta_max:
        ans += int(str(n)[1:n_ketasuu - 1])
        if end <= end_max:
            ans += 1

print(ans)
