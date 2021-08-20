INF = float('inf')
(h, w) = map(int, input().split())
dist = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    s = list(map(int, input().split()))
    for j in range(10):
        if i == j:
            continue
        dist[i][j] = s[j]
for k in range(10):
    for i in range(10):
        for j in range(10):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = 0
for i in range(h):
    T = list(map(int, input().split()))
    for j in range(w):
        if T[j] == -1:
            continue
        if T[j] == 1:
            continue
        ans += dist[T[j]][1]
print(ans)
