import math


def main():
    (x, y, vx, vy, a, b, c, d) = map(int, input().split())
    len = math.sqrt(vx * vx + vy * vy)
    vx /= len
    vy /= len
    print(x + vx * b, y + vy * b)
    print(x - vy * a / 2, y + vx * a / 2)
    print(x - vy * c / 2, y + vx * c / 2)
    print(x - vy * c / 2 - vx * d, y + vx * c / 2 - vy * d)
    print(x + vy * c / 2 - vx * d, y - vx * c / 2 - vy * d)
    print(2 * x - (x - vy * c / 2), 2 * y - (y + vx * c / 2))
    print(2 * x - (x - vy * a / 2), 2 * y - (y + vx * a / 2))


main()
