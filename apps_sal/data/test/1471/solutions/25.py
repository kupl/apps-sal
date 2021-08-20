N = int(input())
ans = [-1] * N
ans[0] = 0
root = [[] for i in range(N)]
for i in range(N - 1):
    (u, v, w) = list(map(int, input().split()))
    root[u - 1].append([v - 1, w])
    root[v - 1].append([u - 1, w])
visited = [0] * N
visited[0] = 1
queue = [0]
while queue:
    x = queue.pop()
    for (i, value) in root[x]:
        if value % 2 == 0:
            ans[i] = ans[x]
        else:
            ans[i] = abs(1 - ans[x])
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)
for i in range(N):
    print(ans[i])
