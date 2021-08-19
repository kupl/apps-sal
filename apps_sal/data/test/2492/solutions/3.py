def d_pairs():
    import numpy as np
    (N, K) = [int(i) for i in input().split()]
    A = np.array([int(i) for i in input().split()], np.int64)
    A = np.sort(A)
    zero = A[A == 0]
    positive = A[A > 0]
    negative = A[A < 0]

    def f(c):
        """数列 A から 2 要素を選んで積を取ったとき、c 以下となるようなペアの選び方"""
        count_pair = 0
        if c >= 0:
            count_pair += len(zero) * N
        count_pair += np.searchsorted(A, c // positive, side='right').sum()
        count_pair += (N - np.searchsorted(A, (-c - 1) // -negative, side='right')).sum()
        count_pair -= np.count_nonzero(A * A <= c)
        return count_pair // 2
    (lower, upper) = (-10 ** 18, 10 ** 18)
    while upper - lower > 1:
        x = (lower + upper) // 2
        if f(x) >= K:
            upper = x
        else:
            lower = x
    return upper


print(d_pairs())
