import sys
from collections import deque


def norm_edge(i, j):
    return (i, j) if i < j else (j, i)

inpt = sys.stdin.read().split('\n')
n, k = list(map(int, inpt[0].split()))
edges = []
for edge_str in inpt[1:n]:
    i, j = tuple([int(x) - 1 for x in edge_str.split()])

    edges.append(norm_edge(i, j))

degree = [0 for _ in range(n)]
neigh = [[] for _ in range(n)]
for i, j in edges:
    degree[i] += 1
    degree[j] += 1
    neigh[i].append(j)
    neigh[j].append(i)

r = sorted(degree)[-(k + 1)]
print(r)

visited = set()
color = {}

q = deque([0])
visited = set([0])
while len(q) > 0:
    i = q.popleft()

    used_color = None
    for j in neigh[i]:
        if j not in visited:
            visited.add(j)
            q.append(j)
        e = norm_edge(i, j)
        if used_color is None and e in color:
            used_color = color[e]
    next_color = 0
    for j in neigh[i]:
        e = norm_edge(i, j)
        if e in color:
            continue

        if next_color == used_color:
            next_color += 1
        color[e] = next_color % r if next_color >= r else next_color
        next_color += 1

print(' '.join([str(color[e] + 1) for e in edges]))


# for i in range(n):
#     print("Node", i)
#     for j in neigh[i]:
#         e = norm_edge(i, j)
#         print("    ", e, color[e])

