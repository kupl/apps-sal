from collections import deque
(N, M) = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    (a, b) = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
ans = [0] * (N + 1)
d = deque([1])
while d:
    c = d.popleft()
    for g in G[c]:
        if not ans[g]:
            d.append(g)
            ans[g] = c
print('Yes')
for i in range(2, N + 1):
    print(ans[i])
