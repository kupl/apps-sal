import math


def main() -> None:
    a, b = input().split()

    print(((int(a) * int(b.replace('.', ''))) // 100))

    return


def __starting_point():
    main()


__starting_point()
