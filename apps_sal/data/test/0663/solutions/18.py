r, x1, y1, x2, y2 = (float(x) for x in input().split())
dest = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
if x1 == x2 and y1 == y2:
    print(0)
else:
    res = 0
    while dest > 0:
        dest -= 2 * r
        res += 1
    print(res)
