a, b, c = list(map(int, input().split()))
x1, y1, x2, y2 = list(map(int, input().split()))
bRange = abs(y2 - y1) + abs(x2 - x1)
if a == 0 or b == 0:
    print(bRange)
else:
    py1 = (-b * y1 - c) / a
    py2 = (-b * y2 - c) / a
    px1 = (-a * x1 - c) / b
    px2 = (-a * x2 - c) / b
    pRange1 = ((x2 - py1)**2 + (px2 - y1)**2)**0.5 + abs(y2 - px2) + abs(py1 - x1)
    pRange2 = ((py2 - py1)**2 + (y2 - y1)**2)**0.5 + abs(py1 - x1) + abs(x2 - py2)
    pRange3 = ((x2 - x1)**2 + (px2 - px1)**2)**0.5 + abs(px1 - y1) + abs(y2 - px2)
    pRange4 = ((py2 - x1)**2 + (y2 - px1)**2)**0.5 + abs(px1 - y1) + abs(x2 - py2)
    print(min(bRange, pRange1, pRange2, pRange3, pRange4))
