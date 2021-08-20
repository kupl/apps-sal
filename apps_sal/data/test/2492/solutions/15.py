def main():
    import numpy as np
    from bisect import bisect_left, bisect_right
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    n = bisect_left(A, 0)
    p = bisect_right(A, 0)
    Negative = np.array(A[:n], dtype=np.int64)
    Positive = np.array(A[p:], dtype=np.int64)
    Number_Negative = len(Negative) * len(Positive)
    Number_Positive = len(Negative) * (len(Negative) - 1) // 2 + len(Positive) * (len(Positive) - 1) // 2
    Number_Zero = N * (N - 1) // 2 - Number_Negative - Number_Positive

    def Ncount(x):
        tmp = 0
        for a in Negative:
            tmp += len(Positive) - bisect_left(Positive, (x + a + 1) // a)
        return tmp

    def Ncount1(x):
        tmp = (len(Positive) - np.searchsorted(Positive, (-x - 1) // -Negative, side='right')).sum()
        return tmp

    def Pcount(x):
        tmp = 0
        for (index, a) in enumerate(Positive):
            tmp += bisect_right(Positive[index + 1:], x // a)
        for (index, b) in enumerate(Negative):
            tmp += len(Negative[index + 1:]) - bisect_left(Negative[index + 1:], (x + b + 1) // b)
        return tmp

    def Pcount1(x):
        tmp = 0
        tmp += np.searchsorted(Positive, x // Positive, side='right').sum()
        tmp += (len(Negative) - np.searchsorted(Negative, (-x - 1) // -Negative, side='rigth')).sum()
        tmp -= np.count_nonzero(Positive * Positive <= x)
        tmp -= np.count_nonzero(Negative * Negative <= x)
        return tmp // 2
    if Number_Negative >= K:
        l = -10 ** 18
        r = 0
        while r - l > 1:
            mid = (l + r) // 2
            if K <= Ncount1(mid):
                r = mid
            else:
                l = mid
        print(r)
        return
    elif Number_Negative < K <= Number_Negative + Number_Zero:
        print(0)
        return
    else:
        l = 0
        r = 10 ** 18
        K -= Number_Negative + Number_Zero
        while r - l > 1:
            mid = (l + r) // 2
            if K <= Pcount1(mid):
                r = mid
            else:
                l = mid
        print(r)


def __starting_point():
    main()


__starting_point()
