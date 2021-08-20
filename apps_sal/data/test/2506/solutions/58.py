from bisect import bisect_left, bisect_right
from itertools import accumulate


def resolve():

    def shake_cnt(x):
        cnt = 0
        pos = 0
        for i in range(N):
            pos = bisect_left(A, x - A[i])
            cnt += N - pos
        return cnt < M
    (N, M) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    ng = 0
    ok = 10 ** 6
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if shake_cnt(mid):
            ok = mid
        else:
            ng = mid
    acc = [0] + list(accumulate(A))
    ans = 0
    for i in range(N):
        pos = bisect_right(A, ng - A[i])
        cnt = N - pos
        ans += cnt * A[i] + (acc[N] - acc[pos])
        M -= cnt
    ans += M * ng
    print(ans)


def __starting_point():
    resolve()


__starting_point()
