def main():
    (W, H, N) = list(map(int, input().split()))
    X = 0
    Y = 0
    for _ in range(N):
        (x, y, a) = list(map(int, input().split()))
        if a == 1:
            X = max(X, x)
        elif a == 2:
            W = min(W, x)
        elif a == 3:
            Y = max(Y, y)
        elif a == 4:
            H = min(H, y)
    S = max(W - X, 0) * max(H - Y, 0)
    print(S)


def __starting_point():
    main()


__starting_point()
