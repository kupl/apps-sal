(N, K) = list(map(int, input().split()))
pts = []
ys = []
for _ in range(N):
    (x, y) = list(map(int, input().split()))
    pts.append((x, y))
    ys.append(y)
pts.sort()
ys.sort()
ans = 10 ** 20
for (i, y1) in enumerate(ys):
    for y2 in ys[i + 1:]:
        for (j, (x1, _)) in enumerate(pts):
            num = 0
            for (x, y) in pts[j:]:
                if y1 <= y <= y2:
                    num += 1
                if num >= K:
                    area = (x - x1) * (y2 - y1)
                    ans = min(ans, area)
                    break
print(ans)
