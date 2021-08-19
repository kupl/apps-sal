import math
coordinates = input().split()
x1 = int(coordinates[0])
y1 = int(coordinates[1])
x2 = int(coordinates[2])
y2 = int(coordinates[3])
if x1 == x2:
    y3 = y1
    y4 = y2
    x3 = x1 + abs(y1 - y2)
    x4 = x2 + abs(y1 - y2)
    print(x3, y3, x4, y4)
elif y1 == y2:
    x3 = x1
    x4 = x2
    y3 = y1 + abs(x1 - x2)
    y4 = y2 + abs(x1 - x2)
    print(x3, y3, x4, y4)
elif abs(x1 - x2) == abs(y1 - y2):
    x3 = x1
    x4 = x2
    y3 = y2
    y4 = y1
    print(x3, y3, x4, y4)
else:
    print(-1)
