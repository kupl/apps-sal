import sys, re
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2
from collections import deque, defaultdict, Counter
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop, heapify
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M, R = MAP()
r = LIST()
ABC = [LIST() for _ in range(M)]

dist_matrix = [[0]*N for _ in range(N)]
for A, B, C in ABC:
	dist_matrix[A-1][B-1] = C
	dist_matrix[B-1][A-1] = C

#for i in range(N):
#	print(dist_matrix[i])

#ワーシャルフロイド法  注意 PyPy非対応!!!!
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
 
graph = csr_matrix(dist_matrix) #隣接行列からcsr行列をつくる
dist_matrix = floyd_warshall(graph, directed=False) #無向の場合directed=False
#dist_matrixの中身はfloatになっているので注意！

#for i in range(N):
#	print(dist_matrix[i])

ans = INF
for x in permutations(r):
	dis = 0
	for i in range(1, R):
		dis += dist_matrix[x[i-1]-1][x[i]-1]
	ans = min(ans, dis)

print((int(ans)))


	

