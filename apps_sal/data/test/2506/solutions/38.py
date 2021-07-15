def e_handshake():
    import numpy as np
    N, M = [int(i) for i in input().split()]
    A = np.array(input().split(), np.int64)
    A.sort()

    def shake_cnt(x):
        # 幸福度が x 以上となるような握手を全て行うときの握手の回数
        # 全体から行わない握手回数を引く
        return N**2 - np.searchsorted(A, x - A).sum()

    # 幸福度の上昇が right 以上となるような握手はすべて行い、
    # left となるような握手はいくつか行って握手回数が M 回になるようにする
    left = 0
    right = 10 ** 6
    while right - left > 1:
        mid = (left + right) // 2
        if shake_cnt(mid) >= M:
            left = mid
        else:
            right = mid

    # 幸福度が right 以上上がるような握手をすべて行ったとして、回数と総和を計算
    X = np.searchsorted(A, right - A)  # 行わない人数
    Acum = np.zeros(N + 1, np.int64)  # 累積和で管理する
    Acum[1:] = np.cumsum(A)
    happiness = (Acum[-1] - Acum[X]).sum() + (A * (N - X)).sum()

    # 幸福度が right 未満の上昇となる握手を、握手回数が M になるまで追加で行う
    shake = N * N - X.sum()
    happiness += (M - shake) * left
    return happiness

print(e_handshake())
