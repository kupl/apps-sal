
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N = inp()

for i in range(N):
    c,S = inpl()
    t1 = S//c
    t2 = t1 + 1
    ans = t1**2 * (c-(S%c)) + t2**2 * ((S%c))
    print(ans)

