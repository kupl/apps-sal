import math


def main():
    a, b, c = input().split(' ')
    a, b, c = int(a), int(b), int(c)
    D = math.sqrt(b * b - 4 * a * c)
    x1, x2 = (-b + D) / (2 * a), (-b - D) / (2 * a)
    if x1 < x2:
        x1, x2 = x2, x1
    print(x1)
    print(x2)


def __starting_point():
    main()


__starting_point()
