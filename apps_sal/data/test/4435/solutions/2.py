n = int(input())
a = list(map(int, input().split()))
adj = []
for _ in range(n):
    adj.append([])
dist = [-1] * n
q = []
for (i, x) in enumerate(a):
    for dx in [+x, -x]:
        if 0 <= i + dx < n:
            if a[i + dx] % 2 == x % 2:
                adj[i + dx].append(i)
            else:
                dist[i] = 1
                q.append(i)
q_index = 0
while q_index < len(q):
    top = q[q_index]
    q_index += 1
    for nei in adj[top]:
        if dist[nei] == -1:
            dist[nei] = dist[top] + 1
            q.append(nei)
print(*dist)
