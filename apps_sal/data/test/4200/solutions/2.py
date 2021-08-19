def main() -> None:
    (n, m) = list(map(int, input().split()))
    products = sorted(list(map(int, input().split())))
    is_able = sum(products) / (4 * m) <= products[-m]
    print('Yes' if is_able else 'No')
    return


def __starting_point():
    main()


__starting_point()
