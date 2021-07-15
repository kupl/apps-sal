import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10


N = list(map(int, list(input())))
K = INT()

n = len(N)

if n < K:
	print((0))
	return

dp = [[[0, 0] for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1

for i in range(n):
	for j in range(n):
		for k in range(2):
			for x in range(10):
				ni, nj, nk = i+1, j, k
				if x != 0:
					nj += 1
				if k == 0:
					if N[i] < x:
						continue
					elif x < N[i]:
						nk = 1
				dp[ni][nj][nk] += dp[i][j][k]

ans = 0

print((dp[n][K][0] + dp[n][K][1]))

