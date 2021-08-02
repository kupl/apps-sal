from collections import deque
N, M = map(int, input().split())

graph = [[] for _ in range(N)]
flag = [0] * N

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

D = deque([0])
visited = [False] * N
visited[0] = True

while D:
    v = D.popleft()
    for i in graph[v]:
        if visited[i]:
            continue
        visited[i] = True
        flag[i] = v
        D.append(i)

print("Yes")
for i in range(1, N):
    print(flag[i] + 1)
