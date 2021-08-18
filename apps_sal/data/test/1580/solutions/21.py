import bisect


def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    return True


n, m = map(int, input().split())
par = [-1] * n

for _ in range(m):
    x, y, z = map(int, input().split())
    unite(x - 1, y - 1)
par.sort()
print(bisect.bisect_left(par, 0))
