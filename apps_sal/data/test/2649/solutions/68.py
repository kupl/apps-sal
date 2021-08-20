def main():
    n = int(input())
    (X, Y) = ([], [])
    for _ in range(n):
        (x, y) = list(map(int, input().split()))
        X.append(x + y)
        Y.append(x - y)
    X.sort()
    Y.sort()
    print(max(X[-1] - X[0], Y[-1] - Y[0]))


def __starting_point():
    main()


__starting_point()
