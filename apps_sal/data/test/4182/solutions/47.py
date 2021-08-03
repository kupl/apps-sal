def __starting_point():
    n, m, x, y = list(map(int, input().split()))
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    X.sort()
    Y.sort()

    flg = False
    # xの場所がYのFROM-に入っていないこと
    if (Y[0] <= x):
        flg = True
    # yの場所がXのFROM-に入っていないこと
    elif (y <= X[n - 1]):
        flg = True
    # Xの右端とYの左端が交わらないこと
    elif (X[n - 1] >= Y[0]):
        flg = True

    if flg:
        print("War")
    else:
        print("No War")


__starting_point()
