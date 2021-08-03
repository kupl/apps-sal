import sys
from collections import deque
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

N, M = map(int, readline().split())
L = [readline().strip() for i in range(N)]


def root(x):
    if x == p[x]:
        return x
    p[x] = y = root(p[x])
    return y


def unite(x, y):
    px = root(x)
    py = root(y)
    if px < py:
        p[py] = px
    else:
        p[px] = py


*p, = range(N + M)
for i in range(N):
    for j, c in enumerate(L[i]):
        if c == '=':
            unite(i, N + j)

G = [[] for i in range(N + M)]
RG = [[] for i in range(N + M)]
deg = [0] * (N + M)

for i in range(N):
    x = root(i)
    for j, c in enumerate(L[i]):
        y = root(N + j)
        if c == '<':
            G[x].append(y)
            RG[y].append(x)
            deg[y] += 1
        elif c == '>':
            G[y].append(x)
            RG[x].append(y)
            deg[x] += 1
A = [-1] * (N + M)

que = deque()
for i in range(N + M):
    if root(i) == i and deg[i] == 0:
        que.append(i)
while que:
    v = que.popleft()
    lb = 0
    for w in RG[v]:
        lb = max(lb, A[w])
    A[v] = lb + 1
    for w in G[v]:
        deg[w] -= 1
        if deg[w] == 0:
            que.append(w)
if any(root(i) == i and A[i] == -1 for i in range(N + M)):
    print("No")
else:
    for i in range(N + M):
        A[i] = A[root(i)]
    print("Yes")
    print(*A[:N])
    print(*A[N:])
