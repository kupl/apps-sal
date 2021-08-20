from collections import deque
(N, M) = map(int, input().split())
graph = [[] for _ in range(N)]
flag = [0] * N
for i in range(M):
    (A, B) = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)
D = deque()
D.append(0)
visited = [False] * N
visited[0] = True
while D:
    v = D.popleft()
    for nv in graph[v]:
        if visited[nv] == True:
            continue
        visited[nv] = True
        flag[nv] = v
        D.append(nv)
print('Yes')
for i in range(1, N):
    print(flag[i] + 1)
