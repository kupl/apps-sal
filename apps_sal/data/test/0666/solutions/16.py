import math


def main():
    q = int(input())

    l = 1
    r = q

    while l < r - 1:
        m = (l + r) // 2

        if (m * (m - 1)) / 2 >= q:
            r = m
        else:
            l = m

    if q == 2:
        print(1)
        return

    print(q - ((l - 1) * (r - 1)) // 2)


def __starting_point():
    main()


__starting_point()
