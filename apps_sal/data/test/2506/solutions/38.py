def e_handshake():
    import numpy as np
    N, M = [int(i) for i in input().split()]
    A = np.array(input().split(), np.int64)
    A.sort()

    def shake_cnt(x):
        return N**2 - np.searchsorted(A, x - A).sum()

    left = 0
    right = 10 ** 6
    while right - left > 1:
        mid = (left + right) // 2
        if shake_cnt(mid) >= M:
            left = mid
        else:
            right = mid

    X = np.searchsorted(A, right - A)
    Acum = np.zeros(N + 1, np.int64)
    Acum[1:] = np.cumsum(A)
    happiness = (Acum[-1] - Acum[X]).sum() + (A * (N - X)).sum()

    shake = N * N - X.sum()
    happiness += (M - shake) * left
    return happiness


print(e_handshake())
