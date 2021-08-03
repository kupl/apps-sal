x1, y1, x2, y2 = map(int, input().split())
if y2 >= y1 and x2 >= x1:
    y3 = y2 + abs(x2 - x1)
    x3 = x2 - abs(y2 - y1)
elif y2 >= y1 and x1 > x2:
    x3 = x2 - abs(y2 - y1)
    y3 = y2 - abs(x2 - x1)
elif y1 > y2 and x2 >= x1:
    x3 = x2 + abs(y2 - y1)
    y3 = y2 + abs(x2 - x1)
elif y1 > y2 and x1 > x2:
    x3 = x2 + abs(y2 - y1)
    y3 = y2 - abs(x2 - x1)

x4 = x1 + x3 - x2
y4 = y1 + y3 - y2

print(x3, y3, x4, y4)
