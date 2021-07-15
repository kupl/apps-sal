
MOD = 10**9+7
from collections import deque
N, = list(map(int, input().split()))
G = [set() for _ in range(N+1)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    G[a].add(b)
    G[b].add(a)

queue=deque([1])
vs = set([1])
dist = [0] * (N+1)
mx = 0
mxv = 1
while queue:
    v = queue.popleft()
    for u in G[v]:
        if u in vs:
            continue
        vs.add(u)
        queue.append(u)
        dist[u] = dist[v] + 1
        if mx < dist[u]:
            mx = dist[u]
            mxv = u

queue=deque([mxv])
vs = set([mxv])
dist2 = [0] * (N+1)
mx2 = 0
mxv2 = 1
while queue:
    v = queue.popleft()
    for u in G[v]:
        if u in vs:
            continue
        vs.add(u)
        queue.append(u)
        dist2[u] = dist2[v] + 1
        if mx2 < dist2[u]:
            mx2 = dist2[u]
            mxv2 = u

queue=deque([mxv2])
vs = set([mxv2])
dist3 = [0] * (N+1)
while queue:
    v = queue.popleft()
    for u in G[v]:
        if u in vs:
            continue
        vs.add(u)
        queue.append(u)
        dist3[u] = dist3[v] + 1
#print(mxv, mxv2)
#print(dist2)
#print(dist3)
r = 0
for i in range(1, N+1):
    x = min(dist2[i], dist3[i])
    r = max(x, r)
# 絶対に良さはr以上になる
#　なぜならx = rとなるノードをどちらの色に塗っても、良さはrに決まるから...

X = [0]*(N+1)
for i in range(1, N+1):
    y = max(dist2[i], dist3[i])
    X[y] += 1

#print(r)
for i in range(N-1, r-1, -1):
    X[i] = X[i] + X[i+1]

#print(X)
# d[i] = dがi以下になる場合の数
X.append(0)
d = [0]*(N+1)
for i in range(N, r-1, -1):
    x = min(N-X[i+1]+1, N)
    d[i] = pow(2, x, MOD) 
#print(d)

R = 0
for i in range(r, N+1):
    R = (R + i*(d[i]-d[i-1]))%MOD
print(R)


