def main():
    X, K, D = list(map(int, input().split()))

    X = abs(X)
    q = X // D
    if q >= K:
        X -= K * D
    else:
        X -= q * D
        if (K - q) % 2 == 1:
            X = abs(X - D)

    print(X)
    return


def __starting_point():
    main()

__starting_point()
