from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = list(map(int, input().split()))
    u, v = u - 1, v - 1
    graph[u].append([v, w])
    graph[v].append([u, w])

colors = [-1 for _ in range(N)]
stack = deque()
stack.append(0)
colors[0] = 0

while stack:
    n = stack.popleft()
    for _next, w in graph[n]:
        if colors[_next] != -1:
            continue
        colors[_next] = (colors[n] + w) % 2
        stack.append(_next)

for c in colors:
    print(c)

