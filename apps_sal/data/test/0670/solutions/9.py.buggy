import math
a, b, c = [int(i) for i in input().split()]
x1, y1, x2, y2 = [int(i) for i in input().split()]
l1 = abs(x1 - x2) + abs(y1 - y2)
if(a == 0 or b == 0):
    print(l1)
    return
xa = -(b * y1 + c) / a
ya = y1
xb = x1
yb = -(a * x1 + c) / b
xc = -(b * y2 + c) / a
yc = y2
xd = x2
yd = -(a * x2 + c) / b
l2 = abs(x1 - xa) + math.sqrt((xa - xc)**2 + (ya - yc)**2) + abs(xc - x2)
l3 = abs(x1 - xa) + math.sqrt((xa - xd)**2 + (ya - yd)**2) + abs(yd - y2)
l4 = abs(y1 - yb) + math.sqrt((xb - xc)**2 + (yb - yc)**2) + abs(xc - x2)
l5 = abs(y1 - yb) + math.sqrt((xb - xd)**2 + (yb - yd)**2) + abs(yd - y2)
print(min(l1, l2, l3, l4, l5))
