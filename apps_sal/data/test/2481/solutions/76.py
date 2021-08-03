h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

dist = []
dist.extend(c)
for i in range(10):
    for j in range(10):
        for k in range(10):
            if dist[j][k] > dist[j][i] + dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]
print(sum(dist[a[i][j]][1] for i in range(h) for j in range(w) if a[i][j] > -1))
