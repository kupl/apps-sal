from bisect import bisect_left
from itertools import accumulate


def resolve():

    def getCount(x):
        count = 0
        for Ai in A:
            idx = bisect_left(A, x - Ai)
            count += N - idx
        return count >= M
    (N, M) = list(map(int, input().split()))
    A = sorted(map(int, input().split()))
    A_r = A[::-1]
    B = [0] + list(accumulate(A_r))
    MIN = 0
    MAX = 2 * 10 ** 5 + 1
    while MAX - MIN > 1:
        MID = (MIN + MAX) // 2
        if getCount(MID):
            MIN = MID
        else:
            MAX = MID
    ans = 0
    count = 0
    for Ai in A_r:
        idx = bisect_left(A, MIN - Ai)
        ans += Ai * (N - idx) + B[N - idx]
        count += N - idx
    print(ans - (count - M) * MIN)


def __starting_point():
    resolve()


__starting_point()
