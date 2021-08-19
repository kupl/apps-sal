(n, k) = list(map(int, input().split()))
ps = [tuple(map(int, input().split())) for i in range(n)]
sx = sorted(ps, key=lambda x: x[0])
nx = list(enumerate(sx))
ans = 5e+18
for (f, (x1, y1)) in nx[:n - k + 1]:
    for (e, (x2, y2)) in nx[f + k - 1:]:
        dx = x2 - x1
        sy = sorted((y for (x, y) in sx[f:e + 1]))
        for (y3, y4) in zip(sy, sy[k - 1:]):
            if y3 <= y1 and y4 >= y2:
                ans = min(ans, dx * (y4 - y3))
print(ans)
