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


(N, M) = map(int, input().split())
par = [-1] * N
for _ in range(M):
    (a, b) = map(int, input().split())
    unite(a - 1, b - 1)
print(-min(par))
