def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    p = find(x)
    q = find(y)
    if p == q:
        return None
    if p > q:
        (p, q) = (q, p)
    par[p] += par[q]
    par[q] = p


def same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


(n, m) = map(int, input().split())
par = [-1 for i in range(n)]
(a, b) = ([], [])
for i in range(m):
    (a_, b_) = map(int, input().split())
    a.append(a_ - 1)
    b.append(b_ - 1)
ans = [0] * m
ans[-1] = (n - 1) * n // 2
for i in range(m - 1, 0, -1):
    if same(a[i], b[i]):
        ans[i - 1] = ans[i]
    else:
        ans[i - 1] = ans[i] - size(a[i]) * size(b[i])
        unite(a[i], b[i])
print(*ans, sep='\n')
