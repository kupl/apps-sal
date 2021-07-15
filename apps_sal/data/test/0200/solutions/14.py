def main():
    a, b = list(map(int, input().split()))
    h = b - a
    a, b = list(map(int, input().split()))
    h -= a * 8
    if h <= 0:
        res = 0
    elif a <= b:
        res = -1
    else:
        a = (a - b) * 12
        res = (h + a - 1) // a
    print(res)


def __starting_point():
    main()

__starting_point()
