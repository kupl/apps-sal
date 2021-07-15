from collections import deque, defaultdict
from copy import deepcopy
import sys
import resource

sys.setrecursionlimit(10**5)

N ,u, v = list(map(int,input().split()))
graph = defaultdict(deque)
for _ in range(1,N):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

depth = dict(list(zip(list(range(1,N+1)),[-1]*N)))

def bfs(s):
    if graph[s]:
        for v in graph[s]:
            if depth[v] == -1:
                depth[v] = depth[s] + 1
                bfs(v)

depth = dict(list(zip(list(range(1,N+1)),[-1]*N)))
depth[v] = 0
bfs(v)
depth_v = deepcopy(depth)

depth = dict(list(zip(list(range(1,N+1)),[-1]*N)))
depth[u] = 0
bfs(u)
depth_u = depth
depth_v = sorted(list(depth_v.items()), key = lambda x:x[0])
depth_u = sorted(list(depth_u.items()), key= lambda x:x[0])

MAX = 0
for v,u in zip(depth_v, depth_u):
    if u[1] < v[1]:
        MAX = max(MAX,v[1])
print((MAX-1))

