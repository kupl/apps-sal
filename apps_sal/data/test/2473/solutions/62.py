(n, k) = map(int, input().split())
xy = [tuple(map(int, input().split())) for _ in range(n)]
ans = 10 ** 50
xy.sort()
for l in range(0, n):
    for r in range(l + k - 1, n):
        y = [xy[i][1] for i in range(l, r + 1)]
        y.sort()
        h = 10 ** 50
        for i in range(len(y) - k + 1):
            h = min(h, y[i + k - 1] - y[i])
        ans = min(ans, h * (xy[r][0] - xy[l][0]))
print(ans)
