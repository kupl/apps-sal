

from collections import deque


N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = list(map(int, input().split()))
    g[u - 1].append([v - 1, w])
    g[v - 1].append([u - 1, w])


que = deque()
seen = [0] + [-1] * (N - 1)
que.append(0)
while que:
    s = que.popleft()
    for v, w in g[s]:
        if seen[v] != -1:
            continue
        seen[v] = seen[s] ^ (w % 2)
        que.append(v)
for i in seen:
    print(i)
