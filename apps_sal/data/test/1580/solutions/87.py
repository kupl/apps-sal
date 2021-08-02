from collections import deque

N, M = map(int, input().split())

edge = [[] for i in range(N)]
for i in range(M):
    x, y, _ = map(int, input().split())
    edge[x - 1].append(y - 1)
    edge[y - 1].append(x - 1)

visited = [False] * N

ans = 0
for i in range(N):
    if visited[i]:
        continue
    else:
        ans += 1

    q = deque([i])
    while q:
        cur = q.popleft()
        visited[cur] = True

        for next in edge[cur]:
            if visited[next]:
                continue
            visited[next] = True
            q.append(next)

print(ans)
