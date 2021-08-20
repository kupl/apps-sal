"""input
7 10 2
7 1
1 3
5 2
6 1
6 5
3 7
5 7
1 2
5 1
1 4
"""
import sys
from collections import defaultdict as dd
import heapq
mod = 10 ** 9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


(n, m, d) = ri()
t = dd(list)
r = [0 for i in range(n + 1)]
vis = [0 for i in range(n + 1)]
for i in range(m):
    (u, v) = ri()
    t[u].append(v)
    t[v].append(u)
for i in range(n + 1):
    r[i] = len(t[i])
final = []


def bfs(sor):
    s = [sor]
    vis[sor] = 1
    while s:
        k = s.pop(-1)
        for i in t[k]:
            if vis[i] == 0:
                vis[i] = 1
                s.append(i)


def bfs2(sor):
    s = [sor]
    vis[sor] = 1
    while s:
        k = s.pop(-1)
        for i in t[k]:
            if vis[i] == 0:
                vis[i] = 1
                s.append(i)
                final.append((k, i))


now = []
for i in t[1]:
    now.append(i)
lk = 0
go = dd(int)
vis[1] = 1
for i in range(len(t[1])):
    if vis[t[1][i]] == 0:
        bfs(t[1][i])
        go[t[1][i]] = 1
        lk += 1
if lk <= d:
    temp = t[1][:]
    t[1] = []
    for i in go:
        t[1].append(i)
        t[i].append(1)
        d -= 1
    for i in temp:
        if go[i] == 1:
            pass
        elif d != 0:
            t[1].append(i)
            t[i].append(1)
            d -= 1
    if d != 0:
        print('NO')
    else:
        vis = [0 for i in range(n + 1)]
        bfs2(1)
        if sum(vis) == n:
            print('YES')
            for i in final:
                print(*i)
        else:
            print('NO')
else:
    print('NO')
