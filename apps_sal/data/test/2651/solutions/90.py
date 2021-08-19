def main():
    MOD = 10 ** 9 + 7
    (N, M) = list(map(int, input().split()))
    (*x,) = list(map(int, input().split()))
    (*y,) = list(map(int, input().split()))
    sx = 0
    for (i, x_) in enumerate(x, 1):
        sx = (sx + x_ * (i - 1 - (N - i))) % MOD
    sy = 0
    for (i, y_) in enumerate(y, 1):
        sy = (sy + y_ * (i - 1 - (M - i))) % MOD
    ans = sx * sy % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
