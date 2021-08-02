def main() -> None:
    n, k = list(map(int, input().split()))

    print((min(n % k, abs(n % k - k))))
    return


def __starting_point():
    main()


__starting_point()
