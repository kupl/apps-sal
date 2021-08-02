import math


def main():
    x, y, vx, vy, s, a, c, d = map(int, input().split(' '))

    l = math.sqrt(vx ** 2 + vy ** 2)

    print(x + a / l * vx, y + a / l * vy)
    print(x - s / 2 / l * vy, y + s / 2 / l * vx)
    print(x - c / 2 / l * vy, y + c / 2 / l * vx)
    print(x - c / 2 / l * vy - d / l * vx, y + c / 2 / l * vx - d / l * vy)
    print(x + c / 2 / l * vy - d / l * vx, y - c / 2 / l * vx - d / l * vy)
    print(x + c / 2 / l * vy, y - c / 2 / l * vx)
    print(x + s / 2 / l * vy, y - s / 2 / l * vx)


main()
