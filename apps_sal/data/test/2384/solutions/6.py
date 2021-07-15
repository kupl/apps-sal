import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
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
INF = float("inf")
mod = 10 ** 9 + 7

N = INT()
A = LIST()

dp = [[0]*3 for _ in range(N+1)]
dp[0][0] = -INF
dp[1][0] = -INF
dp[1][2] = A[0]
for i in range(2, N+1):
	if i%2 == 1:
		dp[i][0] = max(dp[i-1][0], dp[i-2][0]+A[i-1])
		dp[i][1] = max(dp[i-1][1], dp[i-2][1]+A[i-1])
		dp[i][2] = dp[i-2][2]+A[i-1]
	else:
		dp[i][0] = max(dp[i-1][1], dp[i-2][0]+A[i-1])
		dp[i][1] = max(dp[i-1][2], dp[i-2][1]+A[i-1])

print((dp[N][1]))

