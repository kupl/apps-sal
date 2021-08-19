import sys
input = sys.stdin.readline
MOD = 10 ** 9 + 7
(N, M) = list(map(int, input().split()))
X = int(input())
UVW = [[int(x) for x in input().split()] for _ in range(M)]
UVW.sort(key=lambda x: x[2])
root = list(range(N + 1))


def find_root(x):
    y = root[x]
    if x == y:
        return x
    z = find_root(y)
    root[x] = z
    return z


tree = [set() for _ in range(N + 1)]
min_tree_size = 0
for (u, v, w) in UVW:
    ru = find_root(u)
    rv = find_root(v)
    if ru == rv:
        continue
    root[ru] = rv
    min_tree_size += w
    tree[u].add((v, w))
    tree[v].add((u, w))
parent = [[0] * 12 for _ in range(N + 1)]
max_wt = [[0] * 12 for _ in range(N + 1)]
depth = [0] * (N + 1)


def dfs(v=1, p=0, dep=0, w=0):
    parent[v][0] = p
    depth[v] = dep
    max_wt[v][0] = w
    for n in range(1, 11):
        parent[v][n] = parent[parent[v][n - 1]][n - 1]
        max_wt[v][n] = max(max_wt[v][n - 1], max_wt[parent[v][n - 1]][n - 1])
    for (u, w) in tree[v]:
        if u == p:
            continue
        dfs(u, v, dep + 1, w)


dfs()


def max_wt_between(x, y):
    wt = 0
    (dx, dy) = (depth[x], depth[y])
    if dx > dy:
        (x, y) = (y, x)
        (dx, dy) = (dy, dx)
    while dy > dx:
        diff = dy - dx
        step = diff & -diff
        n = step.bit_length() - 1
        wt = max(wt, max_wt[y][n])
        y = parent[y][n]
        dy -= step
    if x == y:
        return wt
    step = 1 << 11
    while step:
        n = step.bit_length() - 1
        (rx, ry) = (parent[x][n], parent[y][n])
        if rx != ry:
            wt = max(wt, max_wt[x][n], max_wt[y][n])
            (x, y) = (rx, ry)
        step >>= 1
    return max(wt, max_wt[x][0], max_wt[y][0])


min_size = []
for (u, v, w) in UVW:
    if (v, w) in tree[u]:
        min_size.append(min_tree_size)
    else:
        x = max_wt_between(u, v)
        min_size.append(min_tree_size + w - x)
sm = sum((1 if s < X else 0 for s in min_size))
eq = sum((1 if s == X else 0 for s in min_size))
gr = sum((1 if s > X else 0 for s in min_size))
if eq == 0:
    answer = 0
elif sm == 0:
    answer = (pow(2, eq, MOD) - 2) * pow(2, gr, MOD) % MOD
else:
    answer = 2 * (pow(2, eq, MOD) - 1) * pow(2, gr, MOD) % MOD
print(answer)
