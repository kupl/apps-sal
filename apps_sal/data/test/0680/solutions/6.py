def medium(a, b, c):
    return a + b + c - max(a, b, c) - min(a, b, c)


def wayy(x1, y1, x2, y2):
    (nx, ny) = (x1, y1)
    if [nx, ny] not in way:
        way.append([nx, ny])
    while nx != x2 or ny != y2:
        if x2 > nx:
            nx += 1
        elif x2 < nx:
            nx -= 1
        if y2 > ny:
            ny += 1
        elif y2 < ny:
            ny -= 1
        if [nx, ny] not in way:
            way.append([nx, ny])


(ax, ay) = map(int, input().split())
(bx, by) = map(int, input().split())
(cx, cy) = map(int, input().split())
way = []
mx = medium(ax, bx, cx)
my = medium(ay, by, cy)
wayy(ax, ay, mx, ay)
wayy(bx, by, mx, by)
wayy(cx, cy, mx, cy)
wayy(mx, ay, mx, my)
wayy(mx, by, mx, my)
wayy(mx, cy, mx, my)
print(len(way))
for elem in way:
    print(*elem)
