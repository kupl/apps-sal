from collections import deque
N, M = map(int, input().split())
INF = -1
dist = [[INF] * 3 for _ in range(N)]
vector = [[] for _ in range(N)]

for i in range(M):
    graf1, graf2 = map(int, input().split())
    vector[graf1 - 1].append(graf2 - 1)
S, T = map(int, input().split())
S, T = S - 1, T - 1

dist[S][0] = 0
q = deque()
q.append((S, 0))
while q:
    v, l = q.popleft()
    for i in vector[v]:
        new_l = (l + 1) % 3
        if dist[i][new_l] != INF:
            continue
        dist[i][new_l] = dist[v][l] + 1
        q.append((i, new_l))

ans = dist[T][0]
if ans == INF:
    print("-1")
else:
    print(int(ans / 3))
