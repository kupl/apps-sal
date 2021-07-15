x0, y0, ax, ay, bx, by = list(map(int, input().split()))
xs, ys, t = list(map(int, input().split()))

def gc(m):
    x = x0 * ax ** m + (ax ** m - 1) * bx // (ax - 1)
    y = y0 * ay ** m + (ay ** m - 1) * by // (ay - 1)
    return x, y

coord = []
for i in range(100):
    coord.append(gc(i))
    if coord[-1][0] > 10**18 or coord[-1][1] > 10**18:
        break


def dist(a, b, c, d):
    return abs(a - c) + abs(b - d)
bans = 0
for i in range(len(coord)):
    px = xs
    py = ys
    timer = 0
    j = i
    ans = 0
    while dist(px, py, coord[j][0], coord[j][1]) + timer <= t:
        timer += dist(px, py, coord[j][0], coord[j][1])
        ans += 1
        px, py = coord[j][0], coord[j][1]
        j += 1
    bans = max(bans, ans)
coord = coord[::-1]
for i in range(len(coord)):
    px = xs
    py = ys
    timer = 0
    j = i
    ans = 0
    while j < len(coord) and dist(px, py, coord[j][0], coord[j][1]) + timer <= t:
        timer += dist(px, py, coord[j][0], coord[j][1])
        ans += 1
        px, py = coord[j][0], coord[j][1]
        j += 1
    bans = max(bans, ans)
print(bans)

