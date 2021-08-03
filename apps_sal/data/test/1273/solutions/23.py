from collections import deque
n = int(input())
tree = [[] for _ in range(n + 1)]
for i in range(1, n):
    a, b = map(int, input().split())
    tree[a].append([b, i])
    tree[b].append([a, i])
queue = deque([[1, 0]])
ans = [0] * (n + 1)
ans[1] = 1
visited = [0] * (n + 1)

while queue:
    v, c = queue.popleft()
    color = 1
    for nv, i in tree[v]:
        if c == color:
            color += 1
        if visited[i] == 1:
            continue
        visited[i] = 1
        queue.append([nv, color])
        ans[i] = color
        color += 1
print(max(ans))
for i in range(1, n):
    print(ans[i])
