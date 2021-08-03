def main():
    A, B, C = list(map(int, input().split()))
    X = [A, B, C]
    X.sort()
    if X[0] == X[2]:
        print((0))
    elif X[0] == X[1]:
        print((X[2] - X[1]))
    elif X[1] == X[2]:
        if (X[1] - X[0]) % 2 == 1:
            print(((X[1] - X[0]) // 2 + 2))
        else:
            print(((X[1] - X[0]) // 2))
    else:
        if (X[1] - X[0]) % 2 == 0:
            print(((X[2] - X[1]) + (X[1] - X[0]) // 2))
        else:
            print(((X[2] - X[1]) + (X[1] - X[0]) // 2 + 2))


def __starting_point():
    main()


__starting_point()
