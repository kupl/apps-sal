n = int(input())
plots = []
for i in range(n):
    x, y = map(int, input().split())
    plots.append((x, y, i))
edges = []
plots.sort(key=lambda x: x[0])
for k in range(n - 1):
    x0, _, i = plots[k]
    x1, _, j = plots[k + 1]
    edges.append((x1 - x0, i, j))

plots.sort(key=lambda x: x[1])
for k in range(n - 1):
    _, y0, i = plots[k]
    _, y1, j = plots[k + 1]
    edges.append((y1 - y0, i, j))


par = [i for i in range(n)]
size = [1 for _ in range(n)]
rank = [0 for _ in range(n)]


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if rank[x] > rank[y]:
        par[y] = x
        size[x] += size[y]
    else:
        par[x] = y
        size[y] += size[x]
        if rank[x] == rank[y]:
            rank[y] += 1


def same(x, y):
    return find(x) == find(y)


def kruskal():
    edges.sort()

    res = 0
    for i in range(len(edges)):
        cost, u, v = edges[i]
        if not same(u, v):
            unite(u, v)
            res += cost

    return res


print(kruskal())
