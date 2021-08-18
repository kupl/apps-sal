def __starting_point():
    n, m, x, y = list(map(int, input().split()))
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    X.sort()
    Y.sort()

    flg = False
    if (Y[0] <= x):
        flg = True
    elif (y <= X[n - 1]):
        flg = True
    elif (X[n - 1] >= Y[0]):
        flg = True

    if flg:
        print("War")
    else:
        print("No War")


__starting_point()
