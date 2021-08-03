def main():
    MOD = 10 ** 9 + 7

    N, M = list(map(int, input().split()))
    *x, = list(map(int, input().split()))
    *y, = list(map(int, input().split()))

    sx = 0
    for i, x_ in enumerate(x, 1):
        sx = (sx + x_ * ((i - 1) - (N - i))) % MOD

    sy = 0
    for i, y_ in enumerate(y, 1):
        sy = (sy + y_ * ((i - 1) - (M - i))) % MOD

    ans = sx * sy % MOD

    print(ans)


def __starting_point():
    main()

# ある矩形の面積は
# (x1-x0)(y1-y0)
# x,yの各要素はx1,x0,y1,y0として何回出現するか?
# 1-indexedで、i番目の要素が
# x1として数えられるのは,
# 相方のx0の候補数 = 1-indexedのx0のインデックス = i-1
# x0として数えられるのは、
# 相方のx1の候補数 = 1-indexedのN-x0のインデックス = N-i


__starting_point()
