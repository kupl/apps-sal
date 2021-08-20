def intersect_area(x1, y1, x2, y2, x3, y3, x4, y4):
    x_overlap1 = min(x2, x4) - max(x1, x3)
    y_overlap1 = min(y2, y4) - max(y1, y3)
    if x_overlap1 > 0 and y_overlap1 > 0:
        return x_overlap1 * y_overlap1
    return 0


(x1, y1, x2, y2) = map(int, input().split())
(x3, y3, x4, y4) = map(int, input().split())
(x5, y5, x6, y6) = map(int, input().split())
a = intersect_area(x1, y1, x2, y2, x3, y3, x4, y4)
b = intersect_area(x1, y1, x2, y2, x5, y5, x6, y6)
c = intersect_area(x1, y1, x2, y2, max(x3, x5), max(y3, y5), min(x4, x6), min(y4, y6))
area = (x2 - x1) * (y2 - y1)
if area - (a + b - c) > 0:
    print('YES')
else:
    print('NO')
