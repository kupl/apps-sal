import math

px, py, vx, vy, a, b, c, d = list(map(int, input().split()))

l = math.sqrt(vx**2 + vy**2)

gx, gy = px + ((-1 * vx * d) / l), py + ((-1 * vy * d) / l)

pts = []
pts.append([px + ((b * vx) / l), py + ((b * vy) / l)])
pts.append([px + ((-1 * (a / 2) * vy) / l), py + ((vx * (a / 2)) / l)])
pts.append([px + ((-1 * vy * (c / 2)) / l), py + ((vx * (c / 2)) / l)])
pts.append([gx + ((-1 * (c / 2) * vy) / l), gy + ((vx * (c / 2)) / l)])
pts.append([gx + (((c / 2) * vy) / l), gy + ((-1 * vx * (c / 2)) / l)])
pts.append([px + ((vy * (c / 2)) / l), py + ((-1 * vx * (c / 2)) / l)])
pts.append([px + (((a / 2) * vy) / l), py + ((-1 * vx * (a / 2)) / l)])

for x in pts:
    print(x[0], x[1])

