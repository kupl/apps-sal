import sys
sys.setrecursionlimit(10 ** 9)
(n, m) = map(int, input().split())
pair = [-1] * n


def find(x):
    if pair[x] < 0:
        return x
    else:
        pair[x] = find(pair[x])
        return pair[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    pair[x] += pair[y]
    pair[y] = x


def size(x):
    x = find(x)
    return -pair[x]


for _ in range(m):
    (x, y) = map(int, input().split())
    x -= 1
    y -= 1
    unite(x, y)
max_size = max(map(size, range(n)))
print(max_size)
