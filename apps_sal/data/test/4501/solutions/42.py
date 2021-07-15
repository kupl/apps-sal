def abc044_c():
    import numpy as np
    n, a = map(int, input().split())
    x = list(map(lambda x: int(x) - a, input().split()))  # 平均ターゲット値を引いておく
    x = np.array(x, dtype=np.int64)

    vrange = n * (a + np.max(x))  # 取りうる値の幅(片側), 広めにとってもかまわない
    dp = np.zeros((n+1, 2*vrange+1), dtype=np.int64)  # DPテーブル
    dp[0, vrange] = 1  # 0枚時点で何も選ばずに総和0(平均ターゲット)になる場合を初期値にセット

    for i in np.arange(n):
        # 1つ前のターンを引き継ぐ
        dp[i+1, :] += dp[i, :]
        if 0 < x[i]:
            # x[i]が正の値、1つ前のx[i]個ぶん左側をスライドして持ってくる
            dp[i+1, x[i]:] += dp[i, :-x[i]]
        elif x[i] < 0:
            # x[i]が負の値、1つ前のx[i]個ぶん右側をスライドして持ってくる
            dp[i+1, :x[i]] += dp[i, -x[i]:]
        else:
            # x[i]がゼロ
            dp[i+1, :] += dp[i, :]

    ans = dp[n, vrange] - 1  # 初期値(何も選ばない)の1通りを除く
    print(ans)

def __starting_point():
    abc044_c()
__starting_point()
