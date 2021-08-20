def main():
    (n, a, b) = map(int, input().split())
    print(b if n * a >= b else n * a)


def __starting_point():
    main()


__starting_point()
