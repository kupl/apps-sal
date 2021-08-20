(x1, y1, x2, y2, x3, y3) = map(int, input().split())
ab = (x1 - x2) ** 2 + (y1 - y2) ** 2
bc = (x3 - x2) ** 2 + (y3 - y2) ** 2
if (x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2) == 0 or ab != bc:
    print('No')
else:
    print('Yes')
