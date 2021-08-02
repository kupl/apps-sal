def d2(p, x, y):
    return (p[0] - x) * (p[0] - x) + (p[1] - y) * (p[1] - y)


n, x1, y1, x2, y2 = list(map(int, input().split()))
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
ans = 10000000000000000
dist1 = [d2(p, x1, y1) for p in a]
dist2 = [d2(p, x2, y2) for p in a]
for i in range(n):
    dd1 = dist1[i]
    dd2 = 0
    for j in range(n):
        if dist1[j] > dd1:
            dd2 = max(dd2, dist2[j])
    ans = min(ans, dd1 + dd2)
ans = min(ans, max(dist1), max(dist2))
print(ans)
