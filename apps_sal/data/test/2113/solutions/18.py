n = int(input())
dist = {}
for i in range(n-1):
    u, v = [int(e) for e in input().split()]
    if u not in dist:
        dist[u] = []
    if v not in dist:
        dist[v] = []
    dist[u].append(v)
    dist[v].append(u)
    if i == 0:
        root = u
a = {}
a[root] = 1
q = [root]
while q:
    top = q.pop()
    for e in dist[top]:
        if e not in a:
            a[e] = -a[top]
            q.append(e)
r = list(a.values()).count(1)
print(r * (n - r) - n + 1)

