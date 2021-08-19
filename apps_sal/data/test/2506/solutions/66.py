def main():
    import numpy as np
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    A = np.array(A)

    def cnt_shake(x):  # 握手の組であって合計パワーがx以上となる組みの数
        return n**2 - np.searchsorted(A, x - A).sum()

    right = 10**10 * 1
    left = -10**10 - 1
    while right - left > 1:
        mid = (left + right) // 2
        if cnt_shake(mid) < m:
            right = mid
        else:
            left = mid

    border = left  # border以上の握手をする
    C = n - np.searchsorted(A, border + 1 - A)
    B = np.cumsum(A[::-1])
    # print(border,A,B,C)

    s, cnt = 0, 0
    for i in range(n):
        if C[i] > 0:
            cnt += C[i]
            s += B[C[i] - 1] + A[i] * C[i]
    s += border * (m - cnt)

    print(s)


def __starting_point():
    main()


__starting_point()
