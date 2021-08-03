import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    N = int(readline())
    A = np.array(read().split(), dtype=np.int64).reshape(N, N)

    INF = 10**15
    ans = 0
    for i in range(N):
        B = A[i, :] + A
        np.fill_diagonal(B, INF)
        B[:, i] = INF
        C = B.min(axis=1)
        C[i] = 0

        if (C < A[i, :]).sum() > 0:
            print((-1))
            return
        else:
            index = C > A[i, :]
            ans += A[i, index].sum()

    print((ans // 2))


def __starting_point():
    main()


__starting_point()
