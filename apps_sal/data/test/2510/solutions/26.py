from collections import deque
(n, m) = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    (a, b) = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
visited = [0] * n


def friends(v):
    stack = deque([v])
    visited[v] = 1
    cnt = 1
    while stack:
        v = stack.popleft()
        for nv in G[v]:
            if visited[nv]:
                continue
            visited[nv] = 1
            stack.append(nv)
            cnt += 1
    return cnt


max_friends = 0
for i in range(n):
    if visited[i]:
        continue
    max_friends = max(max_friends, friends(i))
print(max_friends)
