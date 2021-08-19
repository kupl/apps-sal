from sys import stdin
from collections import deque
from math import sqrt, floor, ceil, log, log2, log10, pi


def ii():
    return int(stdin.readline())


def fi():
    return float(stdin.readline())


def mi():
    return map(int, stdin.readline().split())


def fmi():
    return map(float, stdin.readline().split())


def li():
    return list(mi())


def si():
    return stdin.readline()


(n, e) = mi()
a = [[] for _ in range(n + 1)]
for _ in range(e):
    (x, y) = mi()
    a[x].append(y)
    a[y].append(x)
v = [1] * (n + 1)
c = 0
m = 1
for i in range(1, n + 1):
    if v[i]:
        s = [i]
        if i < m:
            c += 1
        while s != []:
            x = s.pop()
            if v[x]:
                s += a[x]
                v[x] = 0
                if x > m:
                    m = x
print(c)
