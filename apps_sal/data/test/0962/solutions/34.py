from collections import deque
(n, m) = map(int, input().split())
g = [list() for _ in range(n + 1)]
en = [0] * (n + 1)
for _ in range(m):
    (u, v) = map(int, input().split())
    g[u].append(v)
    en[v] += 1
q = deque((i for i in range(1, n + 1) if en[i] == 0))
done = list()
while q:
    v = q.popleft()
    for x in g[v]:
        en[x] -= 1
        if not en[x]:
            q.append(x)
    done.append(v)
print(-1 if len(done) == n else 0)
