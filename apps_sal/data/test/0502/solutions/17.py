(ax, ay, bx, by, cx, cy) = map(int, input().split())
ab2 = (ax - bx) ** 2 + (ay - by) ** 2
bc2 = (bx - cx) ** 2 + (by - cy) ** 2
ans = ab2 == bc2 and (cy - by) * (bx - ax) != (by - ay) * (cx - bx)
print('Yes') if ans else print('No')
