h, w, d = list(map(int, input().split()))
a = [tuple(map(int, input().split())) for _ in range(h)]

inf = 1 << 30

pos = [(0, 0)] * (h * w + 1)
dist = [inf] * (h * w + 1)

for i in range(h):
    for j in range(w):
        pos[a[i][j]] = (i, j)

for i in range(1, h * w):
    if dist[i] == inf:
        dist[i] = 0
        j = i + d
        while j <= h * w:
            dist[j] = dist[j - d] + abs(pos[j][0] - pos[j - d][0]) + \
                abs(pos[j][1] - pos[j - d][1])
            j += d


q = int(input())
for i in range(q):
    l, r = list(map(int, input().split()))
    print((dist[r] - dist[l]))

