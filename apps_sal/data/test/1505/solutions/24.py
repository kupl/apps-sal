from math import *

px, py, vx, vy, a, b, c, d = list(map(int, input().split()))

tri_top = 0, 0 + b
tri_right = 0 + a / 2, 0
tri_left = 0 - a / 2, 0

rect_top_right = 0 + c / 2, 0
rect_top_left = 0 - c / 2, 0
rect_bottom_right = 0 + c / 2, 0 - d
rect_bottom_left = 0 - c / 2, 0 - d

theta = atan2(vx, vy)


def work(pt):
    init_theta = atan2(pt[0], pt[1])
    new_theta = init_theta + theta
    rad = sqrt(pt[0]**2 + pt[1]**2)
    x = sin(new_theta) * rad + px
    y = cos(new_theta) * rad + py
    return str(x) + ' ' + str(y)


print(work(tri_top))
print(work(tri_left))
print(work(rect_top_left))
print(work(rect_bottom_left))
print(work(rect_bottom_right))
print(work(rect_top_right))
print(work(tri_right))
