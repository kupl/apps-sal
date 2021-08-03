def main() -> None:
    s = input()
    t = input()

    print(('Yes' if s == t[:-1] else 'No'))


def __starting_point():
    main()


__starting_point()
