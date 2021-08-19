from collections import deque
(N, M) = list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
for _ in range(M):
    (a, b) = list(map(int, input().split()))
    G[a].append(b)
    G[b].append(a)
q = deque([1])
closed = [False] * (N + 1)
closed[1] = True
Ans = [0] * (N + 1)
while q:
    v = q.popleft()
    for u in G[v]:
        if not closed[u]:
            closed[u] = True
            q.append(u)
            Ans[u] = v
print('Yes')
print('\n'.join(map(str, Ans[2:])))
