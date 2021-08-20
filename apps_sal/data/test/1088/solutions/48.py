MOD = 998244353


def dsFind(ds, x):
    if ds[x] == x:
        return x
    x0 = x
    while ds[x] != x:
        x = ds[x]
    ds[x0] = x
    return x


def dsUnion(ds, x, y):
    xRoot = dsFind(ds, x)
    yRoot = dsFind(ds, y)
    if xRoot != yRoot:
        ds[yRoot] = xRoot
        return True
    return False


def isSwappableCols(M, N, K, c1, c2):
    for i in range(N):
        if M[i][c1] + M[i][c2] > K:
            return False
    return True


def isSwappableRows(M, N, K, r1, r2):
    for i in range(N):
        if M[r1][i] + M[r2][i] > K:
            return False
    return True


def f(M, N, K, isSwappable):
    ds = list(range(N))
    for i in range(N):
        for j in range(i + 1, N):
            if dsFind(ds, i) != dsFind(ds, j) and isSwappable(M, N, K, i, j):
                dsUnion(ds, i, j)
    cnts = {}
    for i in range(N):
        root = dsFind(ds, i)
        if not root in cnts:
            cnts[root] = 0
        cnts[root] += 1
    x = 1
    for c in list(cnts.values()):
        for i in range(2, c + 1):
            x = x * i % MOD
    return x


(N, K) = list(map(int, input().split()))
M = [list(map(int, input().split())) for _ in range(N)]
print(f(M, N, K, isSwappableCols) * f(M, N, K, isSwappableRows) % MOD)
