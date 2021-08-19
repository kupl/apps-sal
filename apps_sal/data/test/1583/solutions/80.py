import math


def main():
    (a, b, x) = list(map(int, input().split()))
    if a * a * b == x:
        print(0)
        return
    mid = a ** 2 * b / 2
    c = x / a ** 2
    if mid == x:
        ans = 90 - math.degrees(math.atan(a / b))
    elif mid < x:
        d = 2 * x / a ** 2 - b
        ans = 90 - math.degrees(math.atan(a / (b - d)))
    else:
        d = 2 * a * c / b
        ans = 90 - math.degrees(math.atan(d / b))
    print(ans)


def __starting_point():
    main()


__starting_point()
