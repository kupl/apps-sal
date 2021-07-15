import sys
from collections import deque
readline = sys.stdin.readline
n = int(readline())
G = [[] for _ in range(n)]
for _ in range(n-1):
    u,v,w = map(int, readline().split())
    G[u-1].append((v-1,w))
    G[v-1].append((u-1,w))

V = [-1]*n
V[0] = 0
que = deque([0])
while que:
    nw = que.popleft()
    for nx,d in G[nw]:
        if V[nx]!=-1: continue
        V[nx] = (V[nw]+d)%2
        que.append(nx)

for v in V:
    print(v)
