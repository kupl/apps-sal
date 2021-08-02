from collections import deque
N, M = map(int, input().split())

graph = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)

S, T = map(int, input().split())
S -= 1
T -= 1

q = deque([])
q.append([S, 0, 0])

seen = [[False] * 3 for i in range(N)]

while q:
    v, cost, step = q.popleft()
    if seen[v][step]:
        continue
    seen[v][step] = True
    if step == 0:
        if v == T:
            print(cost)
            break
        cost += 1
        step = 3
    for u in graph[v]:
        q.append([u, cost, step - 1])
else:
    print(-1)
