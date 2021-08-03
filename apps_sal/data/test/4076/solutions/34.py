import math


def colon():
    A, B, H, M = map(int, input().split())
    h = 30 * H
    h = h - 5.5 * M
    h = min(h, 360 - h)
    h = h * math.pi / 180
    res = A**2 + B**2 - 2 * A * B * math.cos(h)
    print(res**0.5)


colon()
