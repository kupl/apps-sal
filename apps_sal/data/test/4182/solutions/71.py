def __starting_point():
    n, m, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x_max = max(x)
    y_min = min(y)

    flg = False
    for Z in range(X + 1, Y + 1):
        if x_max < Z <= y_min:
            flg = True
            break

    if flg:
        print("No War")
    else:
        print("War")


__starting_point()
