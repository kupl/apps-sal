def main():
    (a, b, c) = list(map(int, input().split()))
    print('YES' if b - a == c - b else 'NO')


def __starting_point():
    main()


__starting_point()
