from collections import defaultdict as di
from collections import deque as dq
n = int(input())
coupl = di(list)
nodess = [int(x) - 1 for x in input().split()]
for i in range(n - 1):
    node = nodess[i]
    coupl[i + 1].append(node)
    coupl[node].append(i + 1)

colors = [int(x) - 1 for x in input().split()]

Q = dq()
found = set()
Q.append((0, 0))
parent = [-1] * n
order = []
while Q:
    node, p = Q.popleft()
    if node in found:
        continue
    found.add(node)
    parent[node] = p
    order.append(node)
    for nei in coupl[node]:
        Q.append((nei, node))

color = [-1] * n
count = 0
for node in order:
    if colors[node] == color[parent[node]]:
        pass
    else:
        count += 1
    color[node] = colors[node]

print(count)
