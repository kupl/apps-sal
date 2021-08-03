from collections import deque
import sys
sys.setrecursionlimit(100000)

UNDEF = 0

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
c = [UNDEF] * (n + 1)
c[1] = 1


def dfs(par, v):
    cur = 1
    for to in g[v]:
        if c[to] != UNDEF:
            continue
        while cur in (c[par], c[v]):
            cur += 1
        c[to] = cur
        cur += 1
        dfs(v, to)


def bfs():
    q = deque([(0, 1)])
    while q:
        cur = 1
        par, v = q.pop()
        for to in g[v]:
            if c[to] != UNDEF:
                continue
            while cur in (c[par], c[v]):
                cur += 1
            c[to] = cur
            cur += 1
            q.appendleft((v, to))


bfs()
print('%d\n%s' % (max(c), ' '.join(map(str, c[1:]))))
