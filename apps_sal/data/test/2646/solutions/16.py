from sys import stdin, stdout
from collections import defaultdict


def bfs(src):
    q = [src]
    par = [-1] * (n + 1)
    vis = [0] * (n + 1)
    ans = []
    while q:
        cur = q.pop(0)
        for neigh in g[cur]:
            if not vis[neigh]:
                vis[neigh] = 1
                q += [neigh]
                par[neigh] = cur
    for i in range(2, n + 1):
        if par[i] == -1:
            print('No')
            return
        ans += [par[i]]
    print('Yes')
    for v in ans:
        print(v)


for i in range(1):
    g = defaultdict(list)
    n, e = list(map(int, stdin.readline().split()))
    for _ in range(e):
        a, b = map(int, stdin.readline().split())
        g[a] += [b]
        g[b] += [a]
    bfs(1)
