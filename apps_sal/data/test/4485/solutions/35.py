from collections import deque
n, m = list(map(int, input().split()))
edges = [[] * n for _ in range(n)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
# print(edges)
d = deque()
d.append(0)
visited = [False] * n
visited[0] = True
from_0 = [0] * n
while d:
    x = d.popleft()
    for child in edges[x]:
        if visited[child]:
            continue
        else:
            visited[child] = True
            d.append(child)
            from_0[child] = from_0[x] + 1
# print(from_0)
if from_0[n - 1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
