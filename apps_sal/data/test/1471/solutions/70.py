import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    edges[u - 1].append((v - 1, w))
    edges[v - 1].append((u - 1, w))

q = deque()
q.append((0, 0))
color = {}
while q:
    node, dist = q.popleft()
    if node in color:
        continue
    if dist % 2 == 0:
        color[node] = 0
    else:
        color[node] = 1
    for n_node, n_dist in edges[node]:
        q.append((n_node, dist + n_dist))

for i in range(N):
    print(color[i])
