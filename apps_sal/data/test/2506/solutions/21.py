def main():
    import numpy as np
    (n, m) = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = np.array(A)

    def cnt_shake(x):
        return n ** 2 - np.searchsorted(A, x - A).sum()
    right = 2 * 10 ** 5 + 1
    left = -1
    while right - left > 1:
        mid = (left + right) // 2
        if cnt_shake(mid) < m:
            right = mid
        else:
            left = mid
    C = n - np.searchsorted(A, right - A)
    B = np.cumsum(A[::-1])
    cnt = C.sum()
    print(np.sum(A * C) + left * (m - cnt) + B[C[np.where(C > 0)] - 1].sum())


def __starting_point():
    main()


__starting_point()
