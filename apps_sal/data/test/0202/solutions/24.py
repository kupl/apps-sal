import math
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
d = 0
xd = math.fabs(x1-x2)
yd = math.fabs(y1-y2)
d =  int(max(xd ,yd))
print(d)
