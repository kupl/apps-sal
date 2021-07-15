def main() -> None:
    s, w = list(map(int, input().split()))

    print(('unsafe' if s <= w else 'safe'))
    return


def __starting_point():
    main()

__starting_point()
