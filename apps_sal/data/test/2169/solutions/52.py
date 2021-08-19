(h, w, d) = list(map(int, input().split()))
aa = [list(map(int, input().split())) for _ in range(h)]
cd = [None] * (h * w)
for y in range(h):
    for x in range(w):
        cd[aa[y][x] - 1] = (x, y)
sc = [None] * (h * w)
sc[:d] = [0] * d
for i in range(d, h * w):
    sc[i] = sc[i - d] + abs(cd[i][0] - cd[i - d][0]) + abs(cd[i][1] - cd[i - d][1])
q = int(input())
for i in range(q):
    (l, r) = [int(x) - 1 for x in input().split()]
    print(sc[r] - sc[l])
