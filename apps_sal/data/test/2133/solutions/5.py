def f():
    return map(int, input().split())


(s, n) = (0, int(input()))
g = [set() for i in range(n + 1)]
c = [0] + list(f())
d = [0] * (n + 1)
for j in range(n - 1):
    (a, b) = f()
    g[a].add(b)
    g[b].add(a)
p = [q for (q, t) in enumerate(g) if len(t) == 1]
while p:
    a = p.pop()
    if not g[a]:
        break
    b = g[a].pop()
    g[b].remove(a)
    if c[a] - c[b]:
        d[a] += 1
    s = max(s, d[b] + d[a])
    d[b] = max(d[b], d[a])
    if len(g[b]) == 1:
        p.append(b)
print(s + 1 >> 1)
