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
# input = sys.stdin.readline
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
if n % 2 == 1:
    ans = 0
else:
    div = 10
    while div <= n:
        ans += n // div
        div *= 5

print(ans)
