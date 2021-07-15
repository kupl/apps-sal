import sys
def int_reader():
    yield from (int(d) for d in sys.stdin.read().split())

ints = int_reader()
n, m, k = [next(ints) for i in range(3)]
special = [next(ints) for i in range(k)]
is_special = [0]*(n+1)
for x in special:
    is_special[x] = 1

edges = []
for i in range(m):
    u, v, w = [next(ints) for j in range(3)]
    edges.append((w, u, v))
edges.sort()

fu = [i for i in range(n+1)]
def find(x):
    S = []
    while fu[x] != x:
        S.append(x)
        x = fu[x]
    for y in S:
        fu[y] = x
    return x
def union(e):
    a, b = find(e[1]), find(e[2])
    if is_special[b]:
        a, b = b, a
    fu[b] = a

ans = 0
for e in edges:
    a, b = find(e[1]), find(e[2])
    if a == b: continue
    if is_special[a] and is_special[b]:
        ans = e[0]
    union(e)
print((str(ans) + ' ') * k)

