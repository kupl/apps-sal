from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N = int(input())
aa = inpl()
aa.append(INF)
ans = 0
tmp = 1

for i in range(1,N+1):
	if aa[i] <= aa[i-1]*2:
		tmp += 1
	else:
		ans = max(tmp,ans)
		tmp = 1

print(ans)

