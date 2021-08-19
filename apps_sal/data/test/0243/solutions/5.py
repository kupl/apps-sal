import sys


def int_reader():
    yield from (int(d) for d in sys.stdin.read().split())


ints = int_reader()
(n, m, k) = [next(ints) for i in range(3)]
sp = {next(ints) for i in range(k)}
edges = []
for i in range(m):
    (u, v, w) = [next(ints) for j in range(3)]
    edges.append((w, u, v))
edges.sort()
fu = [i for i in range(n + 1)]


def find(x):
    S = []
    while fu[x] != x:
        S.append(x)
        x = fu[x]
    for y in S:
        fu[y] = x
    return x


def union(a, b):
    if b in sp:
        (a, b) = (b, a)
    fu[b] = a


ans = 0
for e in edges:
    (a, b) = (find(e[1]), find(e[2]))
    if a == b:
        continue
    if a in sp and b in sp:
        ans = e[0]
    union(a, b)
print((str(ans) + ' ') * k)
