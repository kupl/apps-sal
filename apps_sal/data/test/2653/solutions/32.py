import collections
N,Q = map(int,input().split())
lski = [[] for i in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    lski[a].append(b)
    lski[b].append(a)
countercost = collections.Counter()
for i in range(Q):
    p,x = map(int,input().split())
    countercost[p] += x

dist = [-1] * (N+1)
parent = [-1] * (N+1)
dist[0] = 0
dist[1] = countercost[1]

d = collections.deque()
d.append(1)

while d:
    v = d.popleft()
    for i in lski[v]:
        if parent[a] == b:
            continue
        if dist[i] != -1:
            continue
        parent[b] = a
        dist[i] = dist[v] + countercost[i]
        d.append(i)
dist.pop(0)
ansls = [str(i) for i in dist]
print(' '.join(ansls))
