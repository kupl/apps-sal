(ax, ay, bx, by, cx, cy) = list(map(int, input().split()))
abx = ax - bx
aby = ay - by
cbx = cx - bx
cby = cy - by
cross = abx * cby - aby * cbx
if (ax - bx) ** 2 + (ay - by) ** 2 == (bx - cx) ** 2 + (by - cy) ** 2 and cross != 0:
    print('Yes')
else:
    print('No')
