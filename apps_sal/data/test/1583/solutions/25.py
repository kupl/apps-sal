from math import atan, degrees


def main():
    a, b, x = map(int, input().split())
    if (a**2 * b) / 2 < x:
        area = a * b - x / a
        c = 2 * area / a
        t = c / a
        ans = degrees(atan(t))
    else:
        area = x / a
        c = 2 * area / b
        t = b / c
        ans = degrees(atan(t))
    print(ans)


def __starting_point():
    main()


__starting_point()
