import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2
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
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()

if N == 0:
	print(0)
	return

lim = 32
top = [0]*(lim+1)
bottom = [0]*(lim+1)

for i in range(1, lim+1):
	if i%2:
		t = (i+1)//2
		top[i] = (4**t-1)//3
		bottom[i] = bottom[i-1]
	else:
		b = i//2
		bottom[i] = (4**b-1)*2//3
		top[i] = top[i-1]

digit = [0]*(lim+1)
for i in range(1, lim+1):
	digit[i] = (-2)**(i-1)

if 0 <= N:
	idx = bisect_left(top, N)
else:
	idx = bisect_left(bottom, -N)

ans = ""
for i in range(idx, 0, -1):
	if -bottom[i-1] <= N <= top[i-1]:
		ans += "0"
	else:
		ans += "1"
		N -= digit[i]

print(ans)
