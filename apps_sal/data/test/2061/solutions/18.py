from collections import Counter, defaultdict
(n, m, k) = [int(x) for x in input().split()]
mp = [['.'] * (m + 2)] + [list('.' + input().strip() + '.') for _ in range(n)] + [['.'] * (m + 2)]
uf = {}
for i in range(n + 2):
    for j in range(m + 2):
        uf[i, j] = (i, j)


def find(u):
    if u != uf[u]:
        uf[u] = find(uf[u])
    return uf[u]


def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu != pv:
        uf[pv] = pu


for i in range(n + 2):
    for j in range(m + 2):
        if mp[i][j] == '*':
            continue
        if i <= n and mp[i + 1][j] == '.':
            union((i, j), (i + 1, j))
        if j <= m and mp[i][j + 1] == '.':
            union((i, j), (i, j + 1))
d = defaultdict(int)
f0 = find((0, 0))
for i in range(n + 2):
    for j in range(m + 2):
        if mp[i][j] == '*':
            continue
        f = find((i, j))
        if f != f0:
            d[f] += 1
l = sorted([(v, k) for (k, v) in list(d.items())])
ll = len(l)
ps = set([u for (_, u) in l[:ll - k]])
r = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if mp[i][j] == '.' and find((i, j)) in ps:
            mp[i][j] = '*'
            r += 1
print(r)
print('\n'.join((''.join(m[1:-1]) for m in mp[1:-1])))
