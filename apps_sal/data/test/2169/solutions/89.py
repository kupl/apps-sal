h, w, d = map(int, input().split())
ad = {}
for i in range(h):
    line = list(map(int, input().split()))
    for j in range(w):
        ad[line[j]] = (i, j)
q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

cl = [0] * (h * w + 1)
for i in range(1, h * w + 1):
    if i + d < len(cl):
        f = ad[i]
        t = ad[i + d]
        cl[i + d] = cl[i] + abs(f[0] - t[0]) + abs(f[1] - t[1])

for l, r in lr:
    print(cl[r] - cl[l])
