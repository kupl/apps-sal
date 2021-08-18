def main():
    import numpy as np
    from sys import stdin

    input = stdin.readline

    N, M, Q = list(map(int, input().split()))

    cumsum = np.zeros((N + 1, N + 1), dtype=np.int64)
    L, R = np.array([input().split() for _ in range(M)], dtype=np.int64).T
    np.add.at(cumsum, (L, R), 1)
    np.cumsum(cumsum, axis=0, out=cumsum)
    np.cumsum(cumsum, axis=1, out=cumsum)

    for _ in range(Q):
        p, q = list(map(int, input().split()))
        p -= 1
        print((cumsum[q, q] - cumsum[q, p] - cumsum[p, q] + cumsum[p, p]))


def __starting_point():
    main()


__starting_point()
