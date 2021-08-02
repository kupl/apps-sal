import math


def main():
    a, b, h, m = map(int, input().split(" "))
    r1 = h * 30 + m / 2
    r2 = 6 * m
    r3 = abs(r1 - r2)
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(r3))))


def __starting_point():
    main()


__starting_point()
