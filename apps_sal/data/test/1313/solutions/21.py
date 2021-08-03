def main():
    n1, n2, k1, k2 = map(int, input().split())
    print(("First", "Second")[n2 >= n1])


def __starting_point():
    main()


__starting_point()
