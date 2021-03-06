import sys


def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    else:
        if par[x] > par[y]:
            (x, y) = (y, x)
        par[x] += par[y]
        par[y] = x
        return True


def isdiff(x, y):
    return find(x) != find(y)


def size(x):
    return -par[find(x)]


input = sys.stdin.readline
(n, m) = map(int, input().split())
par = [-1] * n
inconvenience = [n * (n - 1) // 2]
l = [tuple(map(int, input().split())) for _ in range(m)]
for (a, b) in l[::-1][:-1]:
    if isdiff(a - 1, b - 1):
        num = inconvenience[-1] - size(a - 1) * size(b - 1)
        inconvenience.append(num)
        unite(a - 1, b - 1)
    else:
        inconvenience.append(inconvenience[-1])
print(*inconvenience[::-1], sep='\n')
