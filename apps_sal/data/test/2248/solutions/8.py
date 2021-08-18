import math
from collections import deque
import sys
input = sys.stdin.readline
t = 1


def bfs(a, i, dis, vis):
    vis[i] = 1
    pp = deque()
    pp.append(i)
    while len(pp) != 0:

        z = pp[0]
        vis[z] = 1
        pp.popleft()
        for j in a[z]:
            if vis[j] == 0:
                dis[j] = dis[z] + 1
                pp.append(j)


while t > 0:
    t -= 1
    n, m = map(int, input().split())
    a = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    vis = [0 for i in range(n + 1)]
    dis = [0 for i in range(n + 1)]
    bfs(a, 1, dis, vis)
    p = [max(dis), dis.index(max(dis))]
    vis = [0 for i in range(n + 1)]
    dis = [0 for i in range(n + 1)]
    bfs(a, p[1], dis, vis)
    p = [max(dis), dis.index(max(dis))]
    print(p[0])
