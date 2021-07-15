from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

S = input()
K = int(input())

for i in range(K):
	if S[i] == '1':
		continue
	else:
		print((S[i]))
		return

print((S[K-1]))

