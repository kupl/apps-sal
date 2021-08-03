from sys import *
def f(): return map(int, stdin.readline().split())


n, m = f()
g = [[x] for x in range(n + 1)]
p = [0] * (n + 1)
for j in range(m):
    u, v = f()
    g[u].append(v)
    g[v].append(u)
k = 'YES'
for y, t in enumerate(g):
    if not p[y]:
        if any(len(g[x]) != len(t) or any(p[y] for y in g[x]) for x in t):
            k = 'NO'
            break
        for x in t:
            p[x] = 1
print(k)
