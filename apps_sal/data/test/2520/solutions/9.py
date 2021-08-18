def f(): return map(int, input().split())


n, m, k = f()

p = [-1] * n


def root(x):
    while p[x] >= 0:
        x = p[x]
    return x


def unite(x, y):
    x, y = root(x), root(y)
    if x == y:
        return
    if x > y:
        x, y = y, x
    p[x] += p[y]
    p[y] = x


def same(x, y):
    return root(x) == root(y)


def size(x):
    return -p[root(x)]


l = [-1] * n
for _ in range(m):
    a, b = f()
    unite(a - 1, b - 1)
    l[a - 1] -= 1
    l[b - 1] -= 1
for i in range(n):
    l[i] += size(i)
for _ in range(k):
    c, d = f()
    if same(c - 1, d - 1):
        l[c - 1] -= 1
        l[d - 1] -= 1
print(*l)
