import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(readline())

*p, = range(N)
xs = [0] * N
sz = [1] * N


def root(x):
    if x == p[x]:
        return x
    z = p[x]
    p[x] = y = root(p[x])
    xs[x] += xs[z]
    return y


def unite(x, y):
    px = root(x)
    py = root(y)
    if px == py:
        return
    if px < py:
        p[py] = px
        xs[py] = sz[px]
        sz[px] += sz[py]
    else:
        p[px] = py
        xs[px] = sz[py]
        sz[py] += sz[px]


for i in range(N - 1):
    x, y = map(int, readline().split())
    unite(x - 1, y - 1)
cur = 0
ds = [0] * N
for i in range(N):
    root(i)
    if xs[i] == 0:
        ds[i] = cur
        cur += sz[i]
ans = [0] * N
for i in range(N):
    ans[xs[i] + ds[root(i)]] = i + 1
print(*ans)
