def solve(c1, c2, c3, c4):
    if c1 != c4:
        return 0
    if c3 != 0 and c1 == 0:
        return 0
    return 1


def main() -> None:
    c1 = int(input())
    c2 = int(input())
    c3 = int(input())
    c4 = int(input())
    print(solve(c1, c2, c3, c4))


def __starting_point():
    main()


__starting_point()
