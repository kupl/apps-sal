import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, log
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
from decimal import Decimal
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
from decimal import *
 
N = INT()
ab = [LIST() for _ in range(N-1)]
graph = [[] for _ in range(N)]

for a, b in ab:
	graph[a-1].append(b-1)
	graph[b-1].append(a-1)

length = [len(x) for x in graph]
ans = max(length)

color = defaultdict(int)

q = deque([])
cnt = 1
for x in graph[0]:
	q.append((x, 0, cnt))
	cnt += 1

while q:
	n, previous, col = q.popleft()
	cnt = 1
	for x in graph[n]:
		if x == previous:
			color[(n, x)] = col
			color[(x, n)] = col
		else:
			if cnt == col:
				cnt += 1
			color[(n, x)] = cnt
			color[(x, n)] = cnt
			q.append((x, n, cnt))
			cnt += 1

print(ans)
for a, b in ab:
	print((color[(a-1, b-1)]))

