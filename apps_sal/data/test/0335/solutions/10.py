def main():
    n = int(input())
    if (n % 3 == 0) or (n % 3 == 1):
        print(1, 1, n - 2)
    else:
        print(1, 2, n - 3)


def __starting_point():
    main()


__starting_point()
