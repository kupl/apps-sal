import sys
sys.setrecursionlimit(10 ** 9)
(n, m) = map(int, input().split())
root = [-1] * n


def r(x):
    if root[x] < 0:
        return x
    else:
        root[x] = r(root[x])
        return root[x]


def unite(x, y):
    x = r(x)
    y = r(y)
    if x == y:
        return
    root[x] += root[y]
    root[y] = x


def size(x):
    x = r(x)
    return -root[x]


for i in range(m):
    (x, y) = map(int, input().split())
    x -= 1
    y -= 1
    unite(x, y)
max_size = max(map(size, range(n)))
print(max_size)
