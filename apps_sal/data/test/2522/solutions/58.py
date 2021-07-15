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
INF = 10**6#float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N = INT()
A = LIST()
B = LIST()

CA = Counter(A)
CB = Counter(B)

for k in list(CB.keys()):
	if CB[k] > N-CA[k]:
		print("No")
		return
else:
	print("Yes")

B = B[::-1]

j = 0
jdx = 1

for i in range(N):
	if A[i] == B[i]:
		if B[i] == B[j] or B[i] == A[j]:
			j = -1
			jdx = -1
		B[i], B[j] = B[j], B[i]
		j += jdx

print((*B))



