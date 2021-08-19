from collections import deque
(n, m) = map(int, input().split())
route = [[] for _ in range(n + 1)]
for i in range(m):
    (a, b) = map(int, input().split())
    route[a].append(b)
    route[b].append(a)
dist = [0] * (n + 1)
dist[0] = 0
dist[1] = 0
d = deque()
d.append(1)
ans = [0 for _ in range(n + 1)]
while d:
    v = d.popleft()
    for i in route[v]:
        if dist[i] != 0:
            continue
        dist[i] = dist[v] + 1
        ans[i] = v
        d.append(i)
if len(dist[2:]) > 0:
    print('Yes')
    print(*ans[2:], sep='\n')
else:
    print('No')
