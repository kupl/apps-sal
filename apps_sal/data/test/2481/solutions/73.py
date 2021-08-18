h, w = list(map(int, input().split()))
n = 10
dist = [list(map(int, input().split())) for _ in range(n)]
wall = [list(map(int, input().split())) for _ in range(h)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = 0
for i in range(h):
    for j in range(w):
        if wall[i][j] != -1:
            ans += dist[wall[i][j]][1]
print(ans)
