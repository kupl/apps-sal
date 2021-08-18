ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))

if abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) < .0000001:
    print(0)
    return

pos = set()


def t(p1, p2, px):
    return (p2[0] - p1[0] + px[0], p2[1] - p1[1] + px[1])


pos.add(t((ax, ay), (bx, by), (cx, cy)))
pos.add(t((bx, by), (ax, ay), (cx, cy)))
pos.add(t((ax, ay), (cx, cy), (bx, by)))
pos.add(t((cx, cy), (ax, ay), (bx, by)))
pos.add(t((bx, by), (cx, cy), (ax, ay)))
pos.add(t((cx, cy), (bx, by), (ax, ay)))
print(len(pos))
for i in pos:
    print(i[0], i[1])
