import math
(x1, y1, x2, y2) = [int(x) for x in input().split()]
x12 = x2 - x1
y12 = y2 - y1
L = math.sqrt(x12 ** 2 + y12 ** 2)
x3 = x12 - y12 + x1
y3 = x12 + y12 + y1
x4 = -y12 + x1
y4 = x12 + y1
print('{} {} {} {}'.format(x3, y3, x4, y4))
