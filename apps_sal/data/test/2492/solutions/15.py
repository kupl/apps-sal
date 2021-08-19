def main():
    import numpy as np
    from bisect import bisect_left, bisect_right

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()

    n = bisect_left(A, 0)
    p = bisect_right(A, 0)

    Negative = np.array(A[:n], dtype=np.int64)
    Positive = np.array(A[p:], dtype=np.int64)

    Number_Negative = len(Negative) * len(Positive)
    Number_Positive = len(Negative) * (len(Negative) - 1) // 2 + len(Positive) * (len(Positive) - 1) // 2
    Number_Zero = N * (N - 1) // 2 - Number_Negative - Number_Positive

    # print (Number_Negative)
    # print (Negative)
    # print (Number_Positive)
    # print (Positive)
    # print (Number_Zero)

    def Ncount(x):  # x以下の数を数える(x < 0)
        tmp = 0
        for a in Negative:
            tmp += len(Positive) - bisect_left(Positive, (x + a + 1) // a)
        # print (x, tmp)
        return tmp

    def Ncount1(x):
        tmp = (len(Positive) - np.searchsorted(Positive, (-x - 1) // (-Negative), side='right')).sum()
        return tmp

    def Pcount(x):  # x以下の数を数える(x > 0)
        tmp = 0
        for index, a in enumerate(Positive):
            tmp += bisect_right(Positive[index + 1:], x // a)
        for index, b in enumerate(Negative):
            tmp += len(Negative[index + 1:]) - bisect_left(Negative[index + 1:], (x + b + 1) // b)
            # print (bisect_right(Negative[index + 1:], x / b))
        # print (x, tmp)
        return tmp

    def Pcount1(x):
        tmp = 0
        tmp += np.searchsorted(Positive, x // Positive, side='right').sum()
        tmp += (len(Negative) - np.searchsorted(Negative, (-x - 1) // (-Negative), side='rigth')).sum()
        tmp -= np.count_nonzero(Positive * Positive <= x)
        tmp -= np.count_nonzero(Negative * Negative <= x)
        return tmp // 2

    if Number_Negative >= K:
        # ここに二分探索を書く
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
        # ここに二分探索を書く
        l = 0
        r = 10 ** 18
        K -= (Number_Negative + Number_Zero)
        while r - l > 1:
            mid = (l + r) // 2
            if K <= Pcount1(mid):
                r = mid
            else:
                l = mid

        print(r)
        # return

    # print (Pcount(l) + Number_Negative + Number_Zero)
    # print (Pcount(r) + Number_Negative + Number_Zero)


def __starting_point():
    main()


__starting_point()
