import math


def rad(angle):
    return (angle / 180) * math.pi


def dist(a, b, c, d):
    return math.sqrt((a - c) * (a - c) + (b - d) * (b - d))


tt = int(input())
while tt > 0:
    tt -= 1
    n = int(input())
    angle = rad(360 / (2 * n))
    l1, l2 = n // 2, n - n // 2
    px, py = 0, 0
    vx, vy = 1, 0
    ans = 0
    cur = 0
    for i in range(1, n + 1):
        px += vx
        py += vy
        if i == l1 or i == l2:
            ans += dist(0, 0, px, py)
        cur += angle
        vx = math.cos(cur)
        vy = math.sin(cur)
    print(ans / math.sqrt(2))
