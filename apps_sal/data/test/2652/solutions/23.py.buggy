n = int(input())
par = [-1] * n

# this par & rank are initialized lists


def find(x):
    nonlocal par
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x, y = find(x), find(y)
    nonlocal par
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


def size(x):
    return -par[find(x)]


def same(x, y):
    return find(x) == find(y)


p = []
edge = []
for i in range(n):
    x, y = map(int, input().split())
    p.append([x, y, i])
p.sort(key=lambda x: x[0])
for i in range(n - 1):
    x0, _, j = p[i]
    x1, _, k = p[i + 1]
    edge.append([x1 - x0, j, k])

p.sort(key=lambda x: x[1])
for i in range(n - 1):
    _, y0, j = p[i]
    _, y1, k = p[i + 1]
    edge.append([y1 - y0, j, k])

edge.sort()
ans = 0
for i in range(len(edge)):
    cost, u, v = edge[i]
    if not same(u, v):
        unite(u, v)
        ans += cost

print(ans)
