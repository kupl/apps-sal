from math import cos, radians


def answer(a: int, b: int, h: int, m: int) -> float:
    num = abs((60 * h - 11 * m) / 2)
    theta = min(num, 360 - num)
    return pow(pow(a, 2) + pow(b, 2) - 2 * a * b * cos(radians(theta)), 1 / 2)


def main():
    (a, b, h, m) = map(int, input().split())
    print(answer(a, b, h, m))


def __starting_point():
    main()


__starting_point()
