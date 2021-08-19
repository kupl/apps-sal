n, m, k = map(int, input().split())
par = [-1] * (n + 1)


def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])  # 経路圧縮
        return par[x]


def same(x, y):
    return find(x) == find(y)


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    else:
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x


def size(x):
    return -par[find(x)]


g = [[] for _ in range(n + 1)]
b = [[] for _ in range(n + 1)]
for _ in range(m):
    s, t = map(int, input().split())
    unite(s, t)
    g[s].append(t)
    g[t].append(s)
for _ in range(k):
    s, t = map(int, input().split())
    b[s].append(t)
    b[t].append(s)
for i in range(1, n + 1):
    ans = size(i) - 1 - len(g[i])
    for e in b[i]:
        if same(i, e):
            ans -= 1
    print(ans, end=" ")
