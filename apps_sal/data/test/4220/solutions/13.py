def main() -> None:
    k = int(input())
    s = input()
    print(s if len(s) <= k else s[:k] + '...')
    return


def __starting_point():
    main()


__starting_point()
