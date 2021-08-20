from collections import defaultdict
(n, m) = map(int, input().split())
g = defaultdict(set)
c = list(map(int, input().split()))
for _ in range(m):
    (x, y) = map(int, input().split())
    if c[x - 1] != c[y - 1]:
        g[c[x - 1]].add(c[y - 1])
    if c[y - 1] != c[x - 1]:
        g[c[y - 1]].add(c[x - 1])
ma = 0
co = 10 ** 5 + 1
f = 0
for i in g:
    ma = max(ma, len(g[i]))
for i in g:
    if len(g[i]) == ma:
        f += 1
        co = min(co, i)
if f == 0:
    co = min(c)
print(co)
