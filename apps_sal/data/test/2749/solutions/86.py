import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

H, W = MAP()
N = INT()
a = LIST()[::-1]

ans = [[0]*W for _ in range(H)]
tmp = a.pop()
color = 1
cnt = 0
for i in range(H):
    for j in range(W):
        if i%2:
            j = W-j-1
        ans[i][j] = color
        cnt += 1
        if cnt == tmp and a:
            cnt = 0
            tmp = a.pop()
            color += 1

for i in ans:
    print((" ".join([str(x) for x in i])))

