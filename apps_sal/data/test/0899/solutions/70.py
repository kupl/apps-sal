n, m = map(int, input().split())
a, b, c = zip(*[list(map(int, input().split())) for i in range(m)])

dist = [[1e18]*n for i in range(n)]
for i in range(m):
    dist[a[i]-1][b[i]-1] = dist[b[i]-1][a[i]-1] = min(dist[a[i]-1][b[i]-1], c[i])

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
ans = 0
for i in range(m):
    if dist[a[i]-1][b[i]-1]<c[i]:
        ans += 1

print(ans)
