from collections import deque
(n, m) = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(m)]
neighbor = [[] for _ in range(n)]
for edge in edges:
    neighbor[edge[0] - 1].append(edge[1] - 1)
    neighbor[edge[1] - 1].append(edge[0] - 1)
queue = deque()
queue.append(0)
back = [-1] * n
back[0] = 0
while len(queue) > 0:
    vertex = queue.popleft()
    for nei in neighbor[vertex]:
        if back[nei] == -1:
            back[nei] = vertex
            queue.append(nei)
print('Yes')
for i in back[1:]:
    print(i + 1)
