import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
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

N, D, A = MAP()
XH = [LIST() for _ in range(N)]
XH.sort(key=lambda x:x[0])
X, H = list(zip(*XH))
right = [0]*N
for i, x in enumerate(X):
	right[i] = bisect(X, x+2*D)

damage = [0]*(N+1)
ans = 0
for i, (X, H) in enumerate(XH):
	if i != 0:
		damage[i] += damage[i-1]
	H -= damage[i]
	if H > 0:  # 追加攻撃が必要
		n = -(-H//A)
		ans += n
		d = A*n
		damage[i] += d
		damage[right[i]] -= d  # 範囲外の敵
print(ans)

