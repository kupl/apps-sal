def main():
    (w1, h1, w2, h2) = [int(x) for x in input().split()]
    print(w1 + h1 * 2 + w2 + h2 * 2 + w1 - w2 + 4)


def __starting_point():
    main()


__starting_point()
