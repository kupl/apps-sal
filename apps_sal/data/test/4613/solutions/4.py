from collections import deque
from sys import stdin
input = stdin.readline
(N, M) = map(int, input().split())
neighbor = [[] for _ in range(N)]
A = [-1] * M
B = [-1] * M
for i in range(M):
    (a, b) = map(lambda x: int(x) - 1, input().split())
    A[i] = a
    B[i] = b
    neighbor[a].append(b)
    neighbor[b].append(a)
cnt = 0
for i in range(M):
    (a, b) = (A[i], B[i])
    neighbor[a].remove(b)
    neighbor[b].remove(a)
    visited = [False] * N
    queue = deque()
    queue.append(0)
    visited[0] = True
    while queue:
        x = queue.popleft()
        for z in neighbor[x]:
            if not visited[z]:
                visited[z] = True
                queue.append(z)
    if False in visited:
        cnt += 1
    neighbor[a].append(b)
    neighbor[b].append(a)
print(cnt)
