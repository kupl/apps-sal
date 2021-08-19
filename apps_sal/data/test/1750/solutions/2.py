import sys
sys.setrecursionlimit(200000)
n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
s = max([len(p) for p in g]) + 1
print(s)
r = [0] * n


def dfs(v, c, d):
    r[v] = p = c
    for u in g[v]:
        if not r[u]:
            c = c + 1 if c < s else 1
            if c == d:
                c = c + 1 if c < s else 1
            dfs(u, c, p)


if s > 3:
    dfs(0, 1, 0)
else:
    i = 0
    c = 1
    while len(g[i]) != 1:
        i += 1
    for j in range(n):
        r[i] = c
        c = c + 1 if c < s else 1
        if j < n - 1:
            i = g[i][0] if not r[g[i][0]] else g[i][1]
print(' '.join(map(str, r)))
