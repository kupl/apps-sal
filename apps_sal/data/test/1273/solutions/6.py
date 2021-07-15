import sys
from collections import deque

n = int(sys.stdin.readline())
G = [[] for _ in range(n+1)]
G_order = []
for i in range(n-1):
    a,b = map(lambda x:int(x)-1, sys.stdin.readline().split())
    G[a].append(b)
    G_order.append(b)

que = deque([0])
C = [0]*(n+1)
while que:
    nw = que.popleft()
    c = 1
    for nx in G[nw]:
        if c==C[nw]:
            c+=1
        C[nx] = c
        c += 1
        que.append(nx)

print(max(C))
for i in G_order:
    print(C[i])
