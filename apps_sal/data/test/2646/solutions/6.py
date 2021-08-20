from collections import deque
(N, M) = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
    (a, b) = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def bfs(u):
    queue = deque([u])
    ans = [None] * (N + 1)
    d = [None] * (N + 1)
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                ans[i] = v
                queue.append(i)
    return ans


ans = bfs(1)
print('Yes')
for i in range(2, N + 1):
    print(ans[i])
