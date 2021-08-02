import math


def main():
    n = int(input())
    length = int(math.sqrt(n))
    if length * length == n:
        print(length * 4)
    elif length * (length + 1) >= n:
        print((length * 2 + 1) * 2)
    else:
        print((length + 1) * 4)


def __starting_point():
    main()


__starting_point()
