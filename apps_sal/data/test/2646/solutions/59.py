from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

parents = [-1] * (N + 1)
parents[0] = 0
parents[1] = 0

d = deque()
d.append(1)

while d:
    v = d.popleft()
    for i in graph[v]:
        if parents[i] != -1:
            continue
        parents[i] = v
        d.append(i)
ans = parents[1:]
if -1 in parents:
    print('No')
else:
    print('Yes')
    parents.pop(0)
    parents.pop(0)
    for i in parents:
        print(i)
