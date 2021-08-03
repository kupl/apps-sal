import sys
def f(): return map(int, sys.stdin.readline().split())


n, st, sa = f()
st -= 1
sa -= 1
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = f()
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)


def bfs(s):
    l = [-1] * n
    l[s] = 0
    q = [s]
    while q:
        v = q.pop()
        d = l[v] + 1
        for c in g[v]:
            if l[c] < 0:
                l[c] = d
                q += [c]
    return l


lt = bfs(st)
la = bfs(sa)
m = 0
for i in range(n):
    if lt[i] < la[i]:
        m = max(m, la[i])
print(m - 1)
