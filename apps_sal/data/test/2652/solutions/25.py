def kruskal():
    """
    最小全域木のコストを求める
    """
    cost = 0
    edge.sort()
    for (c, u, v) in edge:
        if same(u, v):
            continue
        union(u, v)
        cost += c
    return cost


def find(x):
    """
    xの根を求める
    """
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    """
    xとyの属する集合を併合する
    """
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if par[x] > par[y]:
        (x, y) = (y, x)
    par[x] += par[y]
    par[y] = x
    return True


def same(x, y):
    """
    xとyが同じ集合に属するかを判定する
    """
    return find(x) == find(y)


n = int(input())
(x, y) = ([], [])
for i in range(n):
    (tmp_x, tmp_y) = map(int, input().split())
    x.append([tmp_x, i])
    y.append([tmp_y, i])
x.sort()
y.sort()
edge = []
for i in range(n - 1):
    edge.append([x[i + 1][0] - x[i][0], x[i + 1][1], x[i][1]])
    edge.append([y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]])
par = [-1] * n
print(kruskal())
