def abc044_c():
    # 値入力
    _, A = map(int, input().split())
    X = list(map(lambda x: int(x) - A, input().split()))
    # 初期値
    d = {0: 1}
    for x in X:
        for k, v in list(d.items()):
            d[k + x] = d.get(k + x, 0) + v  # 差分の合計
    ans = d[0] - 1  # 差分合計0で初期値を除く
    print(ans)


def __starting_point():
    abc044_c()


__starting_point()
