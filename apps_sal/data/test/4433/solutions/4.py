n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

root = 0
for i in range(n):
    if len(g[i]) > len(g[root]):
        root = i

uf = [-1 for _ in range(n)]


def find(u):
    if uf[u] < 0:
        return u
    else:
        ans = find(uf[u])
        uf[u] = ans
        return ans


def merge(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return
    if uf[pu] > uf[pv]:
        pu, pv = pv, pu
    uf[pu] += uf[pv]
    uf[pv] = pu


ans = []
for v in g[root]:
    merge(root, v)
    ans.append((root + 1, v + 1))
for i in range(n):
    for v in g[i]:
        if find(i) != find(v):
            merge(i, v)
            ans.append((i + 1, v + 1))
print('\n'.join(map(lambda x: '{} {}'.format(x[0], x[1]), ans)))
