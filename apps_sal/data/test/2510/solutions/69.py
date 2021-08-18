import sys
sys.setrecursionlimit(1000000)


def f(): return map(int, input().split())


N, M = map(int, input().split())

par = [-1] * (N + 1)


def find(x):
    if par[x] < 0:
        return(x)
    else:
        par[x] = find(par[x])
        return(par[x])


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if (par[x] > par[y]):
        x, y = y, x
    par[x] += par[y]
    par[y] = x
    return


for i in range(M):
    a, b = map(int, input().split())
    unite(a, b)

print(-min(par[1:]))
