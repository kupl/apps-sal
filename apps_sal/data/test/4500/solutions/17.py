def main():
    (A, B, C) = list(map(int, input().split()))
    print('Yes' if A + B - C >= 0 else 'No')


def __starting_point():
    main()


__starting_point()
