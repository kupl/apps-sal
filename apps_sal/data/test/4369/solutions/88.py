def main():
    n = int(input())
    if n % 2 == 0:
        print(int(n / 2))
    else:
        print(int(n / 2) + 1)


def __starting_point():
    main()


__starting_point()
