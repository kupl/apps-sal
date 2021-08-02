n = int(input())
xy = [list(map(int, input().split()))for _ in range(n)]


def gaisin(a, b, c, d, e, f):
    if (a - c) * (d - f) == (c - e) * (b - d): return ["ng"]
    aa = a**2
    bb = b**2
    cc = c**2
    dd = d**2
    ee = e**2
    ff = f**2
    py = ((e - a) * (aa + bb - cc - dd) - (c - a) * (aa + bb - ee - ff)) / (2 * ((e - a) * (b - d) - (c - a) * (b - f)))
    if a == c: px = (2 * (b - f) * py - aa - bb + ee + ff) / (2 * (e - a))
    else: px = (2 * (b - d) * py - aa - bb + cc + dd) / (2 * (c - a))
    return ["ok", px, py]


pxy = []
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            gai = gaisin(x1, y1, x2, y2, x3, y3)
            if len(gai) == 1: continue
            _, px, py = gai
            pxy.append([px, py])
for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        px = (x1 + x2) / 2
        py = (y1 + y2) / 2
        pxy.append([px, py])
ans = 10**10
for px, py in pxy:
    ans = min(ans, max(((px - x)**2 + (py - y)**2)**(0.5)for x, y in xy))
print(ans)
