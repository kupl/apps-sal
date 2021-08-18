import sys
n, m = map(int, input().split())
par = [-1] * n
wei = [0] * n

# 重み付きUnion-Find

# xの根を求める


def find(x):
    if par[x] < 0:
        return x
    else:
        px = find(par[x])
        wei[x] += wei[par[x]]
        par[x] = px
        return px

# xの根から距離


def weight(x):
    find(x)
    return wei[x]

# w[y]=w[x]+wとなるようにxとyを併合


def unite(x, y, w):
    w += wei[x] - wei[y]
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        # sizeの大きいほうがx
        if par[x] > par[y]:
            x, y = y, x
            w = -w
        par[x] += par[y]
        par[y] = x
        wei[y] = w
        return True

# xとyが同じ集合に属するかの判定


def same(x, y):
    return find(x) == find(y)

# xが属する集合の個数


def size(x):
    return -par[find(x)]

# x,yが同じ集合に属するときのwei[y]-wei[x]


def diff(x, y):
    return weight(y) - weight(x)


for i in range(m):
    l, r, d = map(int, input().split())
    if same(l - 1, r - 1):
        if d != diff(l - 1, r - 1):
            print('No')
            return
    else:
        unite(l - 1, r - 1, d)

print('Yes')
