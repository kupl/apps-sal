from collections import deque
(N, M) = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(M):
    (a, b) = list(map(int, input().split()))
    G[a - 1].append(b - 1)
K = [0 for i in range(N)]
for i in range(N):
    for p in G[i]:
        K[p] += 1
q = deque((i for i in range(N) if K[i] == 0))
res = []
while q:
    v1 = q.popleft()
    res.append(v1)
    for v2 in G[v1]:
        K[v2] -= 1
        if K[v2] == 0:
            q.append(v2)
if len(res) == N:
    print(-1)
else:
    print(0)
