(h, w, d) = map(int, input().split())
a = []
for _ in range(h):
    a.append(list(map(int, input().split())))
q = int(input())
querys = []
for _ in range(q):
    (l, r) = map(int, input().split())
    querys.append((l - 1, r - 1))
coor = [None] * (h * w)
for i in range(h):
    for j in range(w):
        coor[a[i][j] - 1] = (i, j)
accu = [0] * (h * w)
for i in range(d, h * w):
    (px, py) = coor[i - d]
    (x, y) = coor[i]
    accu[i] = accu[i - d] + abs(x - px) + abs(y - py)
for (l, r) in querys:
    print(accu[r] - accu[l])
