import numpy as np


def get_Negative(K, pos, neg):
    K = len(pos) * len(neg) - K + 1
    l = 0
    r = 10 ** 18 + 10
    while r - l > 1:
        m = (l + r) // 2
        target = m // pos
        x = np.searchsorted(neg, target, side="right").sum()
        if x >= K:
            r = m
        else:
            l = m
    return -r


def get_Positive(K, pos, neg):
    l = 0
    r = 10 ** 18 + 10
    tmp_pos = np.arange(len(pos))
    tmp_neg = np.arange(len(neg))
    while r - l > 1:
        m = (r + l) // 2
        cnt = 0
        if len(pos) > 1:
            t1 = m // pos
            x1 = np.searchsorted(pos, t1, side="right")
            x1 = np.maximum(0, x1 - tmp_pos - 1)
            cnt += x1.sum()
        if len(neg) > 0:
            t2 = m // neg
            x2 = np.searchsorted(neg, t2, side="right")
            x2 = np.maximum(0, x2 - tmp_neg - 1)
            cnt += x2.sum()
        if cnt >= K:
            r = m
        else:
            l = m
    return r


def main():
    N, K = map(int, input().split())
    A = np.array(input().split(), dtype=np.int64)

    positive = A[A > 0]
    negative = -A[A < 0]
    positive.sort()
    negative.sort()

    Npos = len(positive)
    Nneg = len(negative)
    Nzero = N - Npos - Nneg

    P_neg = Npos * Nneg
    P_pos = 0
    if Npos:
        P_pos += Npos * (Npos - 1) // 2
    if Nneg:
        P_pos += Nneg * (Nneg - 1) // 2
    P_zero = N * (N - 1) // 2 - P_pos - P_neg

    if K <= P_neg:
        ans = get_Negative(K, positive, negative)
        return ans
    K -= P_neg
    if K <= P_zero:
        return 0
    K -= P_zero
    ans = get_Positive(K, positive, negative)
    return ans


def __starting_point():
    print(main())


__starting_point()
