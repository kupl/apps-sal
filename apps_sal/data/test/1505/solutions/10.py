import math
s = input()
l = s.split()
px = float(l[0])
py = float(l[1])
vx = float(l[2])
vy = float(l[3])
a = float(l[4])
b = float(l[5])
c = float(l[6])
d = float(l[7])
a2 = a / 2
c2 = c / 2


def getLeft90(x, y):
    return [-y, x]


def getRight90(x, y):
    return [y, -x]


def getEndPoint(bx, by, vx, vy, l):
    vl = math.sqrt(vx * vx + vy * vy)
    ex = l * vx / vl + bx
    ey = l * vy / vl + by
    return [ex, ey]


sol = []
sol.append(getEndPoint(px, py, vx, vy, b))
vLeft = getLeft90(vx, vy)
sol.append(getEndPoint(px, py, vLeft[0], vLeft[1], a2))

p2 = getEndPoint(px, py, vLeft[0], vLeft[1], c2)
sol.append(p2)
sol.append(getEndPoint(p2[0], p2[1], -vx, -vy, d))  # p3
vRight = getRight90(vx, vy)
p5 = getEndPoint(px, py, vRight[0], vRight[1], c2)
sol.append(getEndPoint(p5[0], p5[1], -vx, -vy, d))  # p4
sol.append(p5)
sol.append(getEndPoint(px, py, vRight[0], vRight[1], a2))  # p6


for i in sol:
    print("%.9f %.9f" % (i[0], i[1]))
