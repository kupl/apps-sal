n, m = map(int, input().split())

par = [-1] * n


def find(x):
    if par[x] < 0:
        return x
    par[x] = find(par[x])
    return par[x]


def union(x, y):
    p, q = find(x), find(y)
    if p == q:
        return
    if p > q:
        p, q = q, p
    par[p] += par[q]
    par[q] = p


def size(x):
    return -par[find(x)]


def same(x, y):
    return find(x) == find(y)


bridge = [0] * m
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    bridge[m - i - 1] = (a, b)

sm = (n * (n - 1)) // 2
ans = [0] * m
for i in range(m):
    ans[m - 1 - i] = sm
    a, b = bridge[i][0], bridge[i][1]
    p, q = find(a), find(b)
    if p != q:
        sm -= size(p) * size(q)
    union(a, b)

for i in range(m):
    print(ans[i])
