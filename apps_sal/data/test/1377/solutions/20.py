from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N = inp()
aa = inpl()

maxi = aa.index(N)

for i in range(maxi,N-1):
    if aa[i] < aa[i+1]:
        print('NO')
        return

for i in reversed(list(range(0,maxi))):
    if aa[i] > aa[i+1]:
        print('NO')
        return

print('YES')

