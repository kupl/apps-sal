import numpy as np


def partsolve(A, x, positive, zero, negative):
    """
    :param A:
    :param x:
    :return: Aの積のペアの中で、x以下となるペアの個数
    """
    count = 0
    if x >= 0:
        count = len(zero) * len(A)
    P = x // positive
    Pc = np.searchsorted(A, P, side='right')
    count += Pc.sum()

    N = (-x-1) // -negative
    Nc = np.searchsorted(A, N, side='right')
    Nc = len(A) - Nc
    count += Nc.sum()

    count -= np.count_nonzero(A * A <= x)
    return count // 2

def solve(N, K, As):
    A = np.array(sorted(As), np.int64)
    positive = A[A > 0]
    zero = A[A == 0]
    negative = A[A < 0]

    left = -10 ** 18
    right = 10 ** 18
    while right - left > 1:
        mid = left + (right - left) // 2
        c = partsolve(A, mid, positive, zero, negative)
        if c < K:
            left = mid
        else:
            right = mid
    return right



def __starting_point():
    N, K = tuple(map(int, input().split(" ")))
    As = list(map(int, input().split(" ")))
    print((solve(N, K, As)))


__starting_point()
