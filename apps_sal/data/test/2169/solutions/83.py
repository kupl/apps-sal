h, w, d = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(h)]

pos = [0] * (h*w + 1)
for i in range(h):
    for j in range(w):
        pos[a[i][j]] = (j, i)

dis = [0] * (h*w + 1)
for i in range(h*w+1):
    if i > d:
        x1, y1 = pos[i-d]
        x2, y2 = pos[i]
        dis[i] = abs(x1-x2) + abs(y1-y2) + dis[i-d]

res = []
q = int(input())
for i in range(q):
    l, r = list(map(int, input().split()))

    res.append(dis[r]-dis[l])

print(("\n".join(map(str,res))))

