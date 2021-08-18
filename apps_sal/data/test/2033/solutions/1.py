import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


n, m = list(map(int, input().split()))
g = {}
for i in range(m):
    a, b = list(map(int, input().split()))
    if b - 1 in g:
        g[b - 1].append(a - 1)
    else:
        g[b - 1] = [a - 1]
k = int(input())
way = list([int(x) - 1 for x in input().split()])
bfs = deque()
bfs.append(way[-1])
lvl = [-1] * n
ans = [0] * n
a = [set() for j in range(n)]
lvl[way[-1]] = 0
while bfs:
    v = bfs.popleft()
    for u in g[v]:
        if lvl[u] == -1:
            lvl[u] = lvl[v] + 1
            a[u].add(v)
            bfs.append(u)
        elif lvl[u] == lvl[v] + 1:
            ans[u] = 1
            a[u].add(v)
ansv = 0
ans1 = 0
for v in range(k - 1):
    if k - v - 1 != lvl[way[v]] and way[v + 1] not in a[way[v]]:
        ans1 += 1
    elif k - v - 1 == lvl[way[v]]:
        break
for v in range(k - 1):
    if ans[way[v]] or a[way[v]].pop() != way[v + 1]:
        ansv += 1

print(ans1, ansv)
