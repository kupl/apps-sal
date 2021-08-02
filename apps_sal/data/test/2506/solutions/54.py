from itertools import accumulate
from bisect import bisect_left
import sys
input = sys.stdin.readline


def func(A, N, M, x):
    count = 0
    for Ai in A:
        idx = bisect_left(A, x - Ai)
        count += N - idx
    if count >= M:
        return True
    else:
        return False


def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    A_rev = list(reversed(A))
    B = [0] + list(accumulate(A_rev))

    min_ = 0
    max_ = 2 * 10 ** 5 + 1
    while max_ - min_ > 1:
        mid = (min_ + max_) // 2
        if func(A, N, M, mid):
            min_ = mid
        else:
            max_ = mid

    ans = 0
    count = 0
    for Ai in A_rev:
        idx = bisect_left(A, min_ - Ai)
        ans += Ai * (N - idx) + B[N - idx]
        count += N - idx
    print(ans - (count - M) * min_)


def __starting_point():
    main()


__starting_point()
