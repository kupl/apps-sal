from collections import deque
N = int(input())
conn = [[] for _ in range(N + 1)]
for i in range(N - 1):
    (u, v, w) = [int(x) for x in input().split()]
    conn[u].append([v, w])
    conn[v].append([u, w])
q = deque([1])
d = [-1] * (N + 1)
d[1] = 0
while q:
    u = q.popleft()
    for e in conn[u]:
        (v, w) = (e[0], e[1])
        if d[v] == -1:
            d[v] = d[u] + w
            q.append(v)
for v in range(1, N + 1):
    print(d[v] % 2)
