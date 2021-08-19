(n, m) = map(int, input().split())
g = [list() for _ in range(n)]
for _ in range(m):
    (s, t) = map(int, input().split())
    g[s - 1].append(t - 1)
prop = [0] * n
expc = [10 ** 6] * n
prop[0] = 1
expc[-1] = 0
for i in range(n):
    if not g[i]:
        continue
    t = len(g[i])
    for x in g[i]:
        prop[x] += prop[i] / t
for i in range(n - 1, -1, -1):
    if not g[i]:
        continue
    t = len(g[i])
    f = 0
    for x in g[i]:
        f += expc[x] + 1.0
    f /= t
    expc[i] = f
cans = expc[0]
for i in range(n - 1):
    t = len(g[i])
    if t < 2:
        continue
    c = max((expc[x] for x in g[i]))
    ne = (expc[i] * t - (c + 1)) / (t - 1)
    de = expc[i] - ne
    na = expc[0] - de * prop[i]
    if cans > na:
        cans = na
print(cans)
