(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.insert(0, -1)
g = [[] for i in range(n + 1)]
for i in range(m):
    (u, v) = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
div = [0]
for i in range(1, n + 1):
    s = set()
    for j in g[i]:
        if a[j] != a[i]:
            s.add(a[j])
    div.append(s)
c = {}
for i in range(1, len(a)):
    if a[i] in c:
        c[a[i]].append(i)
    else:
        c[a[i]] = [i]
m = 0
ind = 1000000
for i in c:
    d = set()
    for j in c[i]:
        for k in div[j]:
            d.add(k)
    if len(d) > m:
        ind = i
        m = len(d)
    elif len(d) == m:
        ind = min(ind, i)
print(ind)
