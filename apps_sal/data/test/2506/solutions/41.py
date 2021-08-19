from bisect import bisect_left
from itertools import accumulate


def resolve():

    def getCount(x):
        cnt = 0
        for a in A:
            idx = bisect_left(A, x - a)
            cnt += N - idx
        return cnt >= M
    (N, M) = list(map(int, input().split()))
    A = sorted(map(int, input().split()))
    ng = 10 ** 9
    ok = 0
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if getCount(mid):
            ok = mid
        else:
            ng = mid
    B = [0] + list(accumulate(A))
    ans = 0
    cnt = 0
    for i in range(N):
        idx = bisect_left(A, ok - A[i])
        ans += B[N] - B[idx] + A[i] * (N - idx)
        cnt += N - idx
    rest = (cnt - M) * ok
    print(ans - rest)


def __starting_point():
    resolve()


__starting_point()
