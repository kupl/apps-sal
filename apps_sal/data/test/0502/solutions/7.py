(ax, ay, bx, by, cx, cy) = map(int, input().split())
if (ax - bx) * (cy - by) == (ay - by) * (cx - bx):
    print('No')
elif (ax - bx) ** 2 + (ay - by) ** 2 == (bx - cx) ** 2 + (by - cy) ** 2:
    print('Yes')
else:
    print('No')
