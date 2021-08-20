def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            (x, y) = (y, x)
        par[x] += par[y]
        par[y] = x
        return True


def same(x, y):
    return find(x) == find(y)


def size(x):
    return -par[find(x)]


(n, m) = map(int, input().split())
par = [-1] * n
ans = 0
for i in range(m):
    (X, Y) = map(int, input().split())
    unite(X - 1, Y - 1)
for i in range(n):
    ans = max(size(i), ans)
print(ans)
