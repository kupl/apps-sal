from copy import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, u, v = map(int, input().split())
node = [[]for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    node[a - 1].append(b - 1)
    node[b - 1].append(a - 1)


def dfs(i):
    visited[i] = 1
    for x in node[i]:
        if visited[x] == 0:
            dis[x] = dis[i] + 1
            dfs(x)


inf = 10**9
dis = [inf] * n; dis[u - 1] = 0; visited = [0] * n
dfs(u - 1)
dis2 = []
dis_dash = copy(dis)
dis2.append(dis_dash)
dis[v - 1] = 0; visited = [0] * n
dfs(v - 1)
dis2.append(dis)
cnt = 0
for i in range(n):
    if dis2[0][i] < dis2[1][i]:
        cnt = max(cnt, dis2[1][i])
print(cnt - 1)
