from collections import deque
n = int(input())
a = list(map(int, input().split()))
ans = [-1 for _ in range(n)]
graph = [[] for _ in range(n)]

que = deque([])
for i, x in enumerate(a):
    t = False
    if i + x < n:
        if (a[i + x] % 2) != (a[i] % 2):
            ans[i] = 1
            t = True
        graph[i + x].append(i)
    if i - x >= 0:
        if (a[i - x] % 2) != (a[i] % 2):
            ans[i] = 1
            t = True
        graph[i - x].append(i)
    if t:
        que.append(i)
# print(graph)
while len(que) > 0:
    now = que.popleft()
    for ne in graph[now]:
        if ans[ne] == -1:
            ans[ne] = ans[now] + 1
            que.append(ne)


print(*ans)
