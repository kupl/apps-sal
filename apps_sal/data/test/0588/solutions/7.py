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
points = []

for _ in range(N):
    x,y = inpl()
    t = math.atan2(y,x)
    points.append((t,x,y))

points.sort()

ans = 0
for s,[theta,x,y] in enumerate(points):
    tmpx = tmpy = 0
    for t in range(s,s+N):
        _,tx,ty = points[t%N]
        tmpx += tx
        tmpy += ty
        ans = max(ans,tmpx**2 + tmpy**2)

print((math.sqrt(ans)))

