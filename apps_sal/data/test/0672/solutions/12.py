from math import floor, sqrt


def main():
    (a, b) = list(map(int, input().split()))
    if a == b:
        print('infinity')
    elif a < b:
        print(0)
    else:
        (res, ab) = (0, a - b)
        for x in range(1, floor(sqrt(ab)) + 1):
            if not ab % x:
                if x > b:
                    res += 1
                if b * x < ab != x * x:
                    res += 1
        print(res)


def __starting_point():
    main()


__starting_point()
