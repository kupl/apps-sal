n, m, k = map(int, input().split())
x = list(map(int, input().split()))
e = []
for _ in range(m):
    e.append(tuple(map(int, input().split())))
e.sort(key=lambda x: x[2])

fa = list(range(n + 1))
sz = [0] * (n + 1)
for u in x:
    sz[u] += 1


def find(x):
    while fa[x] != x:
        fa[x] = fa[fa[x]]
        x = fa[x]
    return x


def unite(u, v):
    u, v = map(find, (u, v))
    fa[u] = v
    if u == v:
        return False
    ret = sz[u] > 0 and sz[v] > 0
    sz[v] += sz[u]
    return ret


for ed in e:
    if unite(ed[0], ed[1]):
        ans = ed[2]

print(*[ans] * k)
