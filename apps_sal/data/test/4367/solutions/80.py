def main():
    N, R = map(int, input().split())

    if N >= 10:
        print(R)
    else:
        print(R + (100 * (10 - N)))


def __starting_point():
    main()


__starting_point()
