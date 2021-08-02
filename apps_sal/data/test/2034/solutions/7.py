from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
vertices = [[] for i in range(n + 1)]
visit = [0] * (n + 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    vertices[a].append(b)
    vertices[b].append(a)


def bfs(v):
    visit[v] = 1
    label = 0
    while queue:
        v, p = queue.popleft()
        for u in vertices[v]:
            if not visit[u]:
                visit[u] = 1
                queue.append((u, v))
            elif u != p:
                label = 1
    return label


ans = 0
for i in range(1, n + 1):
    if not visit[i]:
        queue = deque()
        queue.append((i, 0))
    if not visit[i] and not bfs(i):
        ans += 1

sys.stdout.write(str(ans))
