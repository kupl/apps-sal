import math
from functools import reduce


def readGenerator():
    while True:
        tokens = input().split(' ')
        for t in tokens:
            yield t


reader = readGenerator()


def readWord():
    return next(reader)


def readInt():
    return int(next(reader))


def readFloat():
    return float(next(reader))


def readLine():
    return input()


def fib(n, f1, f2, i):
    if n <= f1:
        return i
    return fib(n, f2, f1 + f2, i + 1)


def bin(a, num):
    left = 0
    right = len(a) - 1
    while (right - left) > 1:
        mid = (right + left) // 2
        if a[mid] < num:
            left = mid
        else:
            right = mid

    return a[left] == num or a[right] == num


def lcm(x, y):
    tmp = x
    while (tmp % y) != 0:
        tmp += x
    return tmp


def createGraph(x, y):
    g = []
    for i in range(200):
        g.append([])

    for i in range(100):
        g[i].append((i + 100, y))
        g[i + 100].append((i, y))
        if i > 0:
            g[i].append((i - 1, x))
            g[100 + i].append((i + 99, x))
            g[i].append((i + 99, y))
            g[99 + i].append((i, y))
        if i < 99:
            g[i].append((i + 1, x))
            g[100 + i].append((i + 101, x))

    return g


def solve(a, b, y, x):
    g = createGraph(x, y)

    d = [10 ** 10] * 200
    d[a] = 0

    v = [False] * 200

    for _ in range(200):
        vi = -1
        mn = 10 ** 10
        for j in range(200):
            if d[j] < mn and not v[j]:
                vi = j
                mn = d[j]

        for (dest, t) in g[vi]:
            d[dest] = min(d[dest], d[vi] + t)

        v[vi] = True

    return d[b]


#t = readInt()
# for _ in range(t):
a, b, x, y = [readInt() for _ in range(4)]
print((solve(a - 1, b + 99, x, y)))
