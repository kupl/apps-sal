from sys import stdin
inp = stdin.readline
(n, m) = map(int, inp().split())
g = {x: [] for x in range(1, n + 1)}
for _ in range(m):
    (a, b) = map(int, inp().split())
    g[a].append(b)
ans = 0
for i in range(1, n + 1):
    d = {}
    for j in g[i]:
        for k in g[j]:
            if k != i:
                d[k] = d.get(k, 0) + 1
    for k in d.values():
        ans += k * (k - 1) // 2
print(ans)
