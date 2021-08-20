import sys
sys.setrecursionlimit(10 ** 9)


def f():
    return map(int, sys.stdin.readline().split())


(n, st, sa) = f()
g = [set() for _ in range(n)]
for _ in range(n - 1):
    (a, b) = f()
    g[a - 1].add(b - 1)
    g[b - 1].add(a - 1)


def dfs(l, v, p=-1, d=0):
    l[v] = d
    for c in g[v]:
        if c != p:
            dfs(l, c, v, d + 1)


lt = [0] * n
dfs(lt, st - 1)
la = [0] * n
dfs(la, sa - 1)
print(max((la[i] for i in range(n) if lt[i] < la[i])) - 1)
