x0, y0, ax, ay, bx, by = map(int, input().split())
sx, sy, t = map(int, input().split())
a = [(x0, y0)]
while a[-1][0] < 10 ** 18 and a[-1][1] < 10 ** 18:
    a.append((a[-1][0] * ax + bx, a[-1][1] * ay + by))
mx = 0
for l in range(len(a)):
    for r in range(l, len(a)):
        if abs(a[l][0] - a[r][0]) + abs(a[l][1] - a[r][1]) + min(abs(a[l][0] - sx) + abs(a[l][1] - sy),
                                                                 abs(a[r][0] - sx) + abs(a[r][1] - sy)) <= t:
            mx = max(mx, r - l + 1)
print(mx)
