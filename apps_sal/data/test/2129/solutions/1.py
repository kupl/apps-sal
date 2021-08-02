import sys
from collections import defaultdict

rlines = sys.stdin.readlines()
lines = (l.strip() for l in rlines)


def eucycle(n, m, adj):
    dir_edges = []
    us = list(adj.keys())
    for u in us:
        while adj[u]:
            v0 = u
            v1 = adj[v0].pop()
            adj[v1].remove(v0)
            dir_edges.append((v0, v1))
            while v1 != u:
                v0 = v1
                v1 = adj[v0].pop()
                adj[v1].remove(v0)
                dir_edges.append((v0, v1))
    return dir_edges


def solve(n, m, edges):
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    odds = set(u for u in adj if len(adj[u]) % 2 == 1)

    for odd in odds:
        adj[odd].add(n + 1)
        adj[n + 1].add(odd)
    total = n - len(odds)
    dir_edges = eucycle(n + 1, m, adj)
    return total, dir_edges


t = int(next(lines))

for ti in range(t):
    n, m = [int(s) for s in next(lines).split()]
    edges = []
    for ei in range(m):
        u, v = [int(s) for s in next(lines).split()]
        edges.append((u, v))
    total, ans = solve(n, m, edges)
    print(total)
    print('\n'.join(str(u) + ' ' + str(v) for u, v in ans if u != n + 1 and v != n + 1))
