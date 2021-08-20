from sys import stdin
from math import sqrt
(px, py, vx, vy, a, b, c, d) = map(int, stdin.readline().split())
length = sqrt(vx * vx + vy * vy)
vx = vx / length
vy = vy / length
(vlx, vly) = (-vy, vx)
(vrx, vry) = (vy, -vx)
midcx = px + vx * -d
midcy = py + vy * -d
x = px + vx * b
y = py + vy * b
print(x, y)
x = px + vlx * a / 2
y = py + vly * a / 2
print(x, y)
x = px + vlx * c / 2
y = py + vly * c / 2
print(x, y)
x = midcx + vlx * c / 2
y = midcy + vly * c / 2
print(x, y)
x = midcx + vrx * c / 2
y = midcy + vry * c / 2
print(x, y)
x = px + vrx * c / 2
y = py + vry * c / 2
print(x, y)
x = px + vrx * a / 2
y = py + vry * a / 2
print(x, y)
