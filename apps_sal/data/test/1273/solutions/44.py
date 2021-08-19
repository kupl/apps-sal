import sys
from collections import deque
N = int(input())
E = [tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(N - 1)]
G = [[] for _ in range(N)]
for (a, b) in E:
    G[a].append(b)
colornum = len(G[0])
colors = [{} for _ in range(N)]
todo = deque()
for (i, p) in enumerate(G[0]):
    colors[0][p] = i
    todo.append((0, p))
while todo:
    (pp, p) = todo.popleft()
    colornum = max(colornum, len(G[p]) + 1)
    c = colors[pp][p]
    for np in G[p]:
        c = (c + 1) % colornum
        colors[p][np] = c
        todo.append((p, np))
print(colornum)
for (a, b) in E:
    print(colors[a][b] + 1)
