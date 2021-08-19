def dist1(x_, y_):
    return (x1 - x_) ** 2 + (y1 - y_) ** 2


def dist2(x_, y_):
    return (x2 - x_) ** 2 + (y2 - y_) ** 2


(n, x1, y1, x2, y2) = [int(i) for i in input().split()]
dist = [[0] * 2 for i in range(n)]
for i in range(n):
    (x, y) = [int(i) for i in input().split()]
    dist[i][0] = dist1(x, y)
    dist[i][1] = dist2(x, y)
dist.sort()
now1 = 0
now2 = 0
lel = 0
for i in range(n):
    lel = max(lel, dist[i][1])
ans = lel
mx = [0] * n
mx[n - 1] = 0
for i in range(n - 2, -1, -1):
    mx[i] = max(mx[i + 1], dist[i + 1][1])
for i in range(n - 1, -1, -1):
    now1 = dist[i][0]
    now2 = mx[i]
    if now1 + now2 < ans:
        ans = now1 + now2
print(ans)
