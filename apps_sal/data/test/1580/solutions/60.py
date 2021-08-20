from collections import deque
(N, M) = map(int, input().split())
edge = [[] for _ in range(N)]
for i in range(M):
    (a, b, c) = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
ans = 0
visited = [False] * N
d = deque()
for i in range(N):
    if visited[i] == False:
        visited[i] = True
        d.append(i)
        while len(d) > 0:
            v = d.popleft()
            for w in edge[v]:
                if visited[w] == False:
                    visited[w] = True
                    d.append(w)
        ans += 1
print(ans)
