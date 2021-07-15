# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
UV = [tuple(map(int,input().split())) for _ in range(M)]
S,T = map(int,input().split())

S,T = S-1,T-1

E = [[] for i in range(3*N)]
for u,v in UV:
    u,v = u-1,v-1
    E[u].append(v+N)
    E[u+N].append(v+2*N)
    E[u+2*N].append(v)

from collections import deque
dq = deque([S])
inf = float("inf")
dist = [inf]*(3*N)
dist[S] = 0

while dq:
    v = dq.popleft()
    for e in E[v]:
        if dist[e] != inf:
            continue
        dist[e] = dist[v]+1
        if e==T:
            print(dist[e]//3)
            return
        dq.append(e)

print(-1)
