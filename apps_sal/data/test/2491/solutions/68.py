(v, e) = map(int, input().split())
r = 0
INF = 10 ** 18
edges = [[] for i in range(v)]
(a, b, c) = ([], [], [])
d = [INF for i in range(v)]
for _ in range(e):
    (s, t, d_) = map(int, input().split())
    edges[s - 1].append((t - 1, d_ * -1))
    a.append(s - 1)
    b.append(t - 1)
    c.append(d_ * -1)
f = False
d[r] = 0
for _ in range(v):
    for u in range(v):
        if d[u] != INF:
            for (to, dist) in edges[u]:
                d[to] = min(d[to], d[u] + dist)
nega = [False] * v
for _ in range(v):
    for i in range(e):
        if d[a[i]] == INF:
            continue
        if d[b[i]] > d[a[i]] + c[i]:
            d[b[i]] = d[a[i]] + c[i]
            nega[b[i]] = True
        if nega[a[i]]:
            nega[b[i]] = True
if nega[-1]:
    print('inf')
else:
    print(d[-1] * -1)
