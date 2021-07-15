def main() -> int:
    (n, k) = map(int, input().split())
    head = [i for i in range(k + 1, 0, -1)]
    tail = [i for i in range(k + 2, n + 1, 1)]

    print(' '.join(str(i) for i in head + tail))

    return 0


def __starting_point():
    main()
__starting_point()
