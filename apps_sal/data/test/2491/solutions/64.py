n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, -c))

dist = [float('inf')] * n
dist[0] = 0
for i in range(n - 1):
    for st, en, score in edges:
        if dist[st] == float('inf'):
            continue
        if dist[en] > dist[st] + score:
            dist[en] = dist[st] + score

negative = [False] * n

for loop in range(n):
    for e in edges:
        st, en, score = e
        if dist[st] == float('inf'):
            continue
        if dist[en] > dist[st] + score:
            dist[en] = dist[st] + score
            negative[en] = True
        if negative[st]:
            negative[en] = True

if negative[n - 1]:
    print('inf')
else:
    print(-dist[n - 1])
