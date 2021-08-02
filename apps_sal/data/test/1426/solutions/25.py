from collections import deque

n, m = list(map(int, input().split()))
uv = [list(map(int, input().split())) for _ in range(m)]
s, t = list(map(int, input().split()))

N = 3 * (n + 1)
adj = [[] for _ in range(N)]
for u, v in uv:
    for i in range(3):
        uu = u + i * n
        vv = v + ((i + 1) % 3) * n
        adj[uu].append(vv)

dq = deque([s])
d = [-1] * N
d[s] = 0
while dq:
    u = dq.popleft()
    for v in adj[u]:
        if d[v] == -1:
            d[v] = d[u] + 1
            dq.append(v)

ans = d[t] // 3
print(ans)
