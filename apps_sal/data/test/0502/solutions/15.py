l = list([int(x) for x in input().split()])
(ax, ay, bx, by, cx, cy) = l
d1 = (ax - bx) ** 2 + (ay - by) ** 2
d2 = (cx - bx) ** 2 + (cy - by) ** 2
same_line = cx * (by - ay) - cy * (bx - ax) == ax * by - bx * ay
print('Yes' if d1 == d2 and (not same_line) else 'No')
