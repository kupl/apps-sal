import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N,M= list(map(int,input().split()))
g = defaultdict(list)

for i in range(M):
    u,v = list(map(int,input().split()))
    g[u].append(N + v)
    g[N + u].append(2*N + v)
    g[2*N + u].append(v)
S,T= list(map(int,input().split()))

dq = deque([S])
inf = 10**15
d = [inf for i in range(3*N+1)]
d[S] = 0

while dq:
    v = dq.popleft()
    for nv in g[v]:
        if d[nv] > d[v] + 1:
            d[nv] = d[v] + 1
            dq.append(nv)

if inf == d[T]:
    print((-1))
else:
    print((d[T]//3))




