def main():
    n = int(input())
    print(n - len(set(input())) if n < 27 else -1)


def __starting_point():
    main()


__starting_point()
