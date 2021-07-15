# Union Find

# xの根を求める
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


# xとyの属する集合の併合
def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    else:
        # sizeの大きいほうがx
        if par[x] > par[y]:
            x, y = y, x
        par[x] += par[y]
        par[y] = x
        return True


# xとyが同じ集合に属するかの判定
def same(x, y):
    return find(x) == find(y)


# xが属する集合の個数
def size(x):
    return -par[find(x)]


# 初期化
# 根なら-size,子なら親の頂点
n,m = map(int,input().split())
par = [-1] * n
ans = 0
for i in range(m):
    X,Y = map(int,input().split())
    unite(X-1,Y-1)

for i in range(n):
    ans = max(size(i),ans)
print(ans)
