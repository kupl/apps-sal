def main():
    s = input()
    return "Yes" if len(set(s)) == 2 else "No"


def __starting_point():
    print(main())


__starting_point()
