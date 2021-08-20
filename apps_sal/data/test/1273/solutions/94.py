import sys
from collections import deque
n = int(input())
G = [[] for _ in range(n + 1)]
G_order = []
for i in range(n - 1):
    (a, b) = [int(x) - 1 for x in input().split()]
    G[a].append(b)
    G_order.append(b)
que = deque([0])
colors = [0] * n
while que:
    prt = que.popleft()
    color = 0
    for cld in G[prt]:
        color += 1
        if color == colors[prt]:
            color += 1
        colors[cld] = color
        que.append(cld)
print(max(colors))
for i in G_order:
    print(colors[i])
