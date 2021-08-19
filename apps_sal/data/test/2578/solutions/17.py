import sys


def find(x):
    if node[x] < 0:
        return x
    else:
        node[x] = find(node[x])
        return node[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    ret = False
    if x != y:
        ret = True
        if rank[x] > rank[y]:
            node[x] += node[y]
            node[y] = x
        else:
            node[y] += node[x]
            node[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
    return ret


def is_same(x, y):
    return find(x) == find(y)


def size(x):
    return -node[find(x)]


(n, m) = map(int, input().split())
node = [-1 for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]
query = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]
for a in query:
    if a[0] >= 2:
        for j in a[2:]:
            unite(a[1], j)
for i in range(1, n + 1):
    print(size(i), end=' ')
