def main():
    n, m = list(map(int, input().split()))
    homeworks = tuple(map(int, input().split()))

    print((max(-1, n - sum(homeworks))))
    return


def __starting_point():
    main()

__starting_point()
