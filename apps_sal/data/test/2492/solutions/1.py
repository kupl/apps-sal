import numpy as np


def main():
    N, K = [int(x) for x in input().split()]
    A = np.array(input().split(), np.int64)
    A = np.sort(A)
    minus = A[A<0]
    zero = A[A==0]
    plus = A[A>0]


    def f(x):
        """number of products <=x
        """
        res = 0
        if x >= 0:
            res += len(zero) * N
        # positive
        res += np.searchsorted(A, x // plus, side="right").sum()

        # negative
        res += (N - np.searchsorted(A, (-x-1) // (-minus), side="right")).sum()

        # remove dup
        res -= np.count_nonzero(A*A <= x)
        res //= 2

        return res

    l = -10**18
    r = 10**18

    while l+1 < r:
        mid = (l+r)//2
        if f(mid) >= K:
            r = mid
        else:
            l = mid
    print(r)


def __starting_point():
    main()
__starting_point()
