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


n, k, c = inpm()
s = input()

saisoku = [0] * n
saioso = [0] * n

i = 0
while i < n:
    if s[i] == "x":
        i += 1
        continue
    saisoku[i] = 1
    i += c + 1

if saisoku.count(1) > k:
    return

i = n - 1
while i >= 0:
    if s[i] == "x":
        i -= 1
        continue
    saioso[i] = 1
    i -= c + 1

for i in range(n):
    if saisoku[i] == 1 and saioso[i] == 1:
        print(i + 1)
