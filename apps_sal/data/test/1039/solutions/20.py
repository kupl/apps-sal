from collections import deque
n = int(input())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a].append((b, c))
    G[b].append((a, c))
(Q, k) = tuple(map(int, input().split()))
INF = 10 ** 9 * n + 1
dists = [INF] * n
dists[k - 1] = 0
q = deque([k - 1])
visited = [0] * n
visited[k - 1] = 1
while q:
    node = q.popleft()
    for (to, c) in G[node]:
        if visited[to] == 1:
            continue
        if dists[to] > dists[node] + c:
            dists[to] = dists[node] + c
            q.append(to)
for _ in range(Q):
    (s, g) = tuple(map(int, input().split()))
    print(dists[s - 1] + dists[g - 1])
