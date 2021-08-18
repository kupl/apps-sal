import sys

root = 0
n, m, D = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

if len(g[root]) < D:
    print('NO')
    return

uf = [-1 for _ in range(n)]


def find(uf, u):
    if uf[u] < 0:
        return u
    else:
        ans = find(uf, uf[u])
        uf[u] = ans
        return ans


def merge(uf, u, v):
    pu = find(uf, u)
    pv = find(uf, v)
    if pu == pv:
        return
    if uf[pu] > uf[pv]:
        pu, pv = pv, pu
    uf[pu] += uf[pv]
    uf[pv] = pu


ans = []
in_tree = {}
for v in g[root]:
    merge(uf, root, v)
for i in range(n):
    for v in g[i]:
        if find(uf, i) != find(uf, v):
            merge(uf, i, v)
            ans.append((i + 1, v + 1))
            in_tree[(min(i, v), max(i, v))] = True

children = [[] for _ in range(n)]
par = [-1 for _ in range(n)]


def dfs(s, super_p):
    st = [(s, root)]
    while len(st) > 0:
        u, p = st.pop()
        children[super_p].append(u)
        merge(par, u, super_p)
        for v in g[u]:
            if v != p and (min(u, v), max(u, v)) in in_tree:
                st.append((v, u))


for v in g[root]:
    dfs(v, v)

sz = len(g[root])
for i in range(len(g[root])):
    found = False
    u = g[root][i]
    if sz > D:
        for v in children[u]:
            for w in g[v]:
                if not found and w != root and find(par, w) != find(par, v) and (min(v, w), max(v, w)) not in in_tree:
                    sz -= 1
                    found = True
                    merge(par, v, w)
                    ans.append((v + 1, w + 1))
                    in_tree[(min(v, w), max(v, w))] = True
    if not found:
        ans.append((root + 1, u + 1))

if sz != D:
    print('NO')
else:
    print('YES')
    print('\n'.join(map(lambda x: '{} {}'.format(x[0], x[1]), ans)))
