import math
(x0, y0, ax, ay, bx, by) = map(int, input().split())
(xs, ys, t0) = map(int, input().split())
lix = [x0]
liy = [y0]
for i in range(70):
    lix.append(lix[-1] * ax + bx)
    liy.append(liy[-1] * ay + by)


def mann(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


ans = 0
for i in range(71):
    tot = 0
    count = 0
    (px, py) = (xs, ys)
    for j in range(i, 71):
        dist = mann(px, py, lix[j], liy[j])
        if tot + dist > t0:
            break
        count += 1
        tot += dist
        (px, py) = (lix[j], liy[j])
    ans = max(ans, count)
for i in range(71):
    tot = 0
    count = 0
    (px, py) = (xs, ys)
    for j in range(i, -1, -1):
        dist = mann(px, py, lix[j], liy[j])
        if tot + dist > t0:
            break
        count += 1
        tot += dist
        (px, py) = (lix[j], liy[j])
    ans = max(ans, count)
print(ans)
