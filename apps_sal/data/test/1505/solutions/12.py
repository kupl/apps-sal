from math import sin, cos, atan2, sqrt, pi
px, py, vx, vy, a, b, c, d = [float(i) for i in input().split()]

angle = atan2(vy,vx)


def rotate(x0, y0, x, y, alpha):
    local_x = x - x0
    local_y = y - y0
    point_angle = atan2(local_y, local_x)

    length = sqrt((x - x0)**2.0 + (y - y0)**2.0)
    return x0 + length * sin(point_angle + alpha), y0 - length * cos(point_angle + alpha)


r0 = px, py + b
r6 = px + a/2.0, py
r5 = px + c/2.0, py
r4 = px + c/2.0, py - d
r3 = px - c/2.0, py - d
r2 = px - c/2.0, py
r1 = px - a/2.0, py

points = [r0, r1, r2, r3, r4, r5, r6]

for point in points:
    new_point = rotate(px, py, point[0], point[1], angle)
    print(" ".join(map(str, new_point)))


