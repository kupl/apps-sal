from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    edges[u - 1].append(v - 1)
s, t = map(int, input().split())
inf = 100000000000
score = [[inf] * 3 for i in range(n)]
now = deque()
now.append(s - 1)
score[s - 1][0] = 0


def bfs(dep, l):
    nonlocal n, m, edges, s, t, score, inf, now
    f = False
    for i in range(l):
        ne = now.popleft()
        for j in edges[ne]:
            if score[j][dep % 3] == inf:
                score[j][dep % 3] = dep
                now.append(j)
    l_ne = len(now)
    if l_ne:
        bfs(dep + 1, l_ne)


bfs(1, 1)
if score[t - 1][0] != inf:
    print(score[t - 1][0] // 3)
else:
    print(-1)
