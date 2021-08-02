from collections import deque


def dfs(s):
    stack = deque([s])
    dist[s] = 0
    while stack:
        v = stack.pop()
        for d, u in E[v]:
            if dist[u] is None:
                dist[u] = dist[v] + d
                stack.append(u)
            else:
                if dist[u] != dist[v] + d:
                    return False
    return True


N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
    l, r, d = map(int, input().split())
    E[l - 1].append((d, r - 1))
    E[r - 1].append((-d, l - 1))
dist = [None] * N
for i in range(N):
    if dist[i] is not None:
        continue
    if not dfs(i):
        print('No')
        break
else:
    print('Yes')
