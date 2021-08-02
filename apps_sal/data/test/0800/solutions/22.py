import math

n = int(input())

coors = [[int(item) for item in input().split(' ')] for i in range(n)]


def get_pos(item):
    (x, y) = item

    deg = math.degrees(math.atan(abs(math.inf if x == 0 else y / x)))

    if y < 0:
        if x >= 0:
            return 360 - deg
        else:
            return 180 + deg
    else:
        if x >= 0:
            return deg
        else:
            return 180 - deg


angles = [get_pos(item) for item in coors]

angles.sort()

t = [angles[0] + 360 - angles[-1]]

for i in range(1, n):
    t.append(angles[i] - angles[i - 1])

print(360 - max(t))
