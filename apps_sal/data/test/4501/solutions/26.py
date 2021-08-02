def abc044_c():
    N, A = map(int, input().split())
    X = list(map(lambda x: int(x) - A, input().split()))  # 平均ターゲットを引いた状態
    dp = [dict() for _ in range(N + 1)]  # 負の値を取り得るため、配列でなく辞書で持つ
    dp[0][0] = 1  # 0枚時点で何も選ばない、を初期値とする
    for i, x in enumerate(X):
        dp[i + 1] = dp[i].copy()  # 前の状態を引き継ぐ
        for val, cnt in dp[i].items():
            dp[i + 1][val + x] = dp[i].get(val + x, 0) + cnt  # 前のターンのxシフト分を加算
    ans = dp[N][0] - 1
    print(ans)


def __starting_point():
    abc044_c()


__starting_point()
