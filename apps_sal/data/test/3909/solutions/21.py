def main():
    n, p = int(input()), 3
    while not n % p:
        p *= 3
    print(n // p + 1)


def __starting_point():
    main()


__starting_point()
