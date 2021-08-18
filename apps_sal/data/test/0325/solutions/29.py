import sys
input = sys.stdin.readline
n, m, p = [int(j) for j in input().split()]


def bellman_ford(v, s, e):
    INF = 10**18
    d = [INF] * v
    d[s] = 0
    for _ in range(v):
        f = False
        for a, b, c in e:
            cost = d[a] + c
            if cost < d[b]:
                d[b] = cost
                f = True
        if not f:
            break
    else:
        print((-1))
        return
    print((max(-d[-1], 0)))


def dfs(edge, s):
    use = {s}
    q = [s]
    while q:
        v = q.pop()
        for w in edge[v]:
            if w in use:
                continue
            use.add(w)
            q.append(w)
    return use


l = [[] for i in range(n)]
ll = [[] for i in range(n)]
e = []
for i in range(m):
    a, b, c = [int(j) for j in input().split()]
    l[a - 1].append(b - 1)
    ll[b - 1].append(a - 1)
    e.append((a - 1, b - 1, p - c))
use = dfs(l, 0) & dfs(ll, n - 1)
e = [(a, b, c) for a, b, c in e if (a in use and b in use)]


bellman_ford(n, 0, e)
