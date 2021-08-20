(n, x1, y1, x2, y2) = list(map(int, input().split()))
l = list()
for i in range(n):
    (x, y) = list(map(int, input().split()))
    z1 = (x - x1) ** 2 + (y - y1) ** 2
    z2 = (x - x2) ** 2 + (y - y2) ** 2
    l.append((z1, z2))
l = sorted(l, key=lambda x: x[0])
ans = max([x[1] for x in l])
ans = min(ans, l[-1][0])
r2 = 0
for i in range(n - 2, -1, -1):
    r1 = l[i][0]
    r2 = max(r2, l[i + 1][1])
    ans = min(ans, r1 + r2)
print(ans)
