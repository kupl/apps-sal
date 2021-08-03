import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
p = [-1] * n


def find(x):
    if p[x] < 0:
        return x
    else:
        p[x] = find(p[x])
        return p[x]


def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    p[x] += p[y]
    p[y] = x


def size(x):
    x = find(x)
    return -p[x]


for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    unite(x, y)

max_size = max(map(size, range(n)))
print(max_size)
