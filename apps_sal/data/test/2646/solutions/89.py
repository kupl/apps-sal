from collections import deque
(N, M) = map(int, input().split())
l = [[] for i in range(N)]
for i in range(M):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    l[a].append(b)
    l[b].append(a)
visited = [-1] * N
visited[0] = 1
que = deque([0])
while que:
    node = que.popleft()
    for i in l[node]:
        if visited[i] == -1:
            visited[i] = node + 1
            que.append(i)
if -1 in visited:
    print('No')
else:
    print('Yes')
    for i in range(1, N):
        print(visited[i])
