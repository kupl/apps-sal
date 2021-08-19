from collections import deque
n = int(input())
graph = []
for i in range(n):
    graph.append([])
for i in range(n - 1):
    (x, y) = [int(s) for s in input().split(' ')]
    graph[x - 1].append(y - 1)
    graph[y - 1].append(x - 1)
seq = [int(s) - 1 for s in input().split(' ')]
visited = [False] * n
levels = [0] * n
positions = [0] * n
for (i, item) in enumerate(seq):
    positions[item] = i
for item in graph:
    item.sort(key=lambda x: positions[x])
stack = deque()
ok_route = True
route_pos = 0
stack.append(0)
output_seq = []
while len(stack):
    next_ = stack.popleft()
    visited[next_] = True
    output_seq.append(next_)
    for item in graph[next_]:
        if not visited[item]:
            stack.append(item)
if output_seq == seq:
    print('Yes')
else:
    print('No')
