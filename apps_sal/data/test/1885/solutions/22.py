def main():
    n = int(input())
    A = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) // (5 * 4 * 3 * 2 * 1)
    B = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) // (6 * 5 * 4 * 3 * 2 * 1)
    C = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) * (n - 6) // (7 * 6 * 5 * 4 * 3 * 2 * 1)
    print(A + B + C)


def __starting_point():
    main()


__starting_point()
