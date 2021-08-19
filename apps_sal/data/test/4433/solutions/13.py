(n, m) = list(map(int, input().split()))
g = [[] for i in range(n + 1)]
ans = set()
for i in range(m):
    (x, y) = list(map(int, input().split()))
    if y > x:
        (x, y) = (y, x)
    g[x].append(y)
    g[y].append(x)
im = 0
mx = 0
used = [False] * (n + 1)
for i in range(1, n + 1):
    if len(g[i]) > mx:
        mx = len(g[i])
        im = i
rip = set()
q = [im]
k = 0
d = [0] * (n + 1)
d[im] = 1
while len(q) > k:
    for v in g[q[k]]:
        if d[v] == 0:
            print(v, q[k])
            d[v] = 1
            q.append(v)
    k += 1
