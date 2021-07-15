from collections import deque

n, m = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

que = deque()
que.append(0)

visited = [0 for _ in range(n)]
visited[0] = 1
ans = [None for _ in range(n)]

print('Yes')
while len(que) > 0:
    c = que.popleft()
    for ne in graph[c]:
        if visited[ne] == 1:
            continue
        que.append(ne)
        ans[ne] = c
        # print(f'ans[{ne}] = {c}')
        visited[ne] = 1

for i in range(1, n):
    print((ans[i] + 1))

