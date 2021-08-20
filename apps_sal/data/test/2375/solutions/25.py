def main():
    (X, Y) = list(map(int, input().split(' ')))
    if abs(X - Y) > 1:
        print('Alice')
    else:
        print('Brown')


def __starting_point():
    main()


__starting_point()
