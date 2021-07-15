def main():
    l = [c == '#' for _ in range(4) for c in input()]
    for sq in ((0, 1, 4, 5), (1, 2, 5, 6), (2, 3, 6, 7), (4, 5, 8, 9), (5, 6, 9, 10),
               (6, 7, 10, 11), (8, 9, 12, 13), (9, 10, 13, 14), (10, 11, 14, 15)):
        if sum(l[i] for i in sq) != 2:
            print('YES')
            return
    print('NO')


def __starting_point():
    main()

__starting_point()
