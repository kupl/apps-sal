
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N,M = inpl()
aa = sorted(inpl())

ra = [[0]*(N//M+3) for _ in range(M)]

# ra [m][n]  : %M == m

for m in range(M):
    c = m
    n = 1
    while c < N:
        ra[m][n] += ra[m][n-1] + aa[c]
        n += 1
        c += M

ans = [0]*(N)
for i in range(N):
    ans[i] = ans[i-1] + aa[i] + ra[i%M][i//M]

print(' '.join(map(str,ans)))

