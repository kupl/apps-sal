def d_pairs():
    # 参考: https://maspypy.com/atcoder-参加感想-2019-02-16abc-155
    import numpy as np
    N, K = [int(i) for i in input().split()]
    A = np.array([int(i) for i in input().split()], np.int64)

    A = np.sort(A)
    zero = A[A == 0]
    positive = A[A > 0]
    negative = A[A < 0]

    def f(c):
        """数列 A から 2 要素を選んで積を取ったとき、c 以下となるようなペアの選び方"""
        count_pair = 0

        # a (数列の要素) == 0 かつ c >= 0 なら、a * x <= c となる x は数列の任意の要素
        if c >= 0:
            count_pair += len(zero) * N
        # a > 0 の場合
        count_pair += np.searchsorted(A, c // positive, side='right').sum()
        # a < 0 の場合 (全体から引くようにすると、見通しがよい)
        count_pair += (N - np.searchsorted(A, (-c - 1) // (-negative), side='right')).sum()
        # 添字の順序に制約があることを反映する
        count_pair -= np.count_nonzero(A * A <= c)  # 「添字が同じ要素を 2 度選んだ場合」を引く
        return count_pair // 2

    # 数列から要素を 2 個選んで積を取ったとき、制約からあり得る値の範囲
    lower, upper = -10 ** 18, 10 ** 18
    while upper - lower > 1:
        x = (lower + upper) // 2
        if f(x) >= K:
            upper = x
        else:
            lower = x
    return upper

print(d_pairs())
