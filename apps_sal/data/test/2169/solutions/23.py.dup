h, w, d = map(int, input().split())
arr = [0] * (h * w + 1)

a = [list(map(int, input().split())) for _ in range(h)]

for i in range(h):
    for j in range(w):
        s = a[i][j]
        arr[s] = (i, j)

q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

cnt = h * w
result = [[0] for _ in range(d)]
for i in range(d):
    l = i
    score = 0
    while l + d <= cnt:
        if l == 0:
            result[i].append(score)
            l += d
            continue
        (ux, uy) = arr[l]
        (vx, vy) = arr[l + d]
        score += (abs(vx - ux) + abs(vy - uy))
        result[i].append(score)
        l += d


for l, r in lr:
    ans = result[l % d]
    print(ans[r // d] - ans[l // d])
