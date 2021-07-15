a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
p = []
if b != 0:
    p.append((x1, -(a * x1 + c) / b))
    p.append((x2, -(a * x2 + c) / b))
if a != 0:
    p.append((-(b * y1 + c) / a, y1))
    p.append((-(b * y2 + c) / a, y2))
p2 = []
for x, y in p:
    if min(x1, x2) - 0.0001 < x < max(x1, x2) + 0.0001 and min(y1, y2) - 0.0001 < y < max(y1, y2) + 0.0001:
        p2.append((x, y))
p3 = []
for x0, y0 in p2:
    for x, y in p3:
        if max(abs(x - x0), abs(y - y0)) < 0.0001:
            break
    else:
        p3.append((x0, y0))
if len(p3) < 2:
    print(abs(x1 - x2) + abs(y1 - y2))
else:
    r0 = abs(x1 - x2) + abs(y1 - y2)
    (ax, ay), (bx, by) = p3
    d = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
    r1 = abs(x1 - ax) + abs(y1 - ay) + d + abs(bx - x2) + abs(by - y2)
    r2 = abs(x1 - bx) + abs(y1 - by) + d + abs(ax - x2) + abs(ay - y2)
    print(min(r0, r1, r2))
