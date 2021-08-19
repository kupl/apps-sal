def R():
    return map(int, input().split())


(n, m) = R()
v = list(R())
g = [set() for i in range(n + 1)]
for i in range(m):
    (x, y) = R()
    g[x].add(y)
    g[y].add(x)
s = 0
for (w, i) in sorted(zip(v, range(1, n + 1)), reverse=True):
    for j in g[i]:
        s += v[j - 1]
        g[j].remove(i)
print(s)
