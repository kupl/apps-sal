def abc144_e():
    import numpy as np
    (N, K) = map(int, input().split())
    A = np.array(input().split(), dtype=np.int64)
    F = np.array(input().split(), dtype=np.int64)
    A = np.sort(A)
    F = np.sort(F)[::-1]
    low = -1
    up = 10 ** 12
    while up - low > 1:
        v = (up + low) // 2
        x = A - v // F
        if x[x > 0].sum() > K:
            low = v
        else:
            up = v
    print(up)


def __starting_point():
    abc144_e()


__starting_point()
