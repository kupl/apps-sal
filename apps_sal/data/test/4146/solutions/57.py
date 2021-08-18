import sys
import bisect
import math
import itertools
import string
import queue
import copy
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
def inp(): return int(input())
def inpm(): return list(map(int, input().split()))
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])


n = inp()
a = inpl()

cnt_even = Counter(a[::2]).most_common() + [(0, 0)]
cnt_odd = Counter(a[1::2]).most_common() + [(0, 0)]

ans = 0
if cnt_even[0][0] == cnt_odd[0][0]:
    ans = n - max(cnt_even[0][1], cnt_odd[0][1]) - max(cnt_even[1][1], cnt_odd[1][1])
else:
    ans = n - cnt_even[0][1] - cnt_odd[0][1]

print(ans)
