
from bisect import bisect_left
from itertools import accumulate


def resolve():
    def getCount(x):
        cnt = 0
        for a in A:
            # X未満の個数
            idx = bisect_left(A, x - a)
            # X以上の個数
            cnt += N - idx
        # X以上を使う！と決めた時、M個以上になるか
        return cnt >= M

    N, M = list(map(int, input().split()))
    A = sorted(map(int, input().split()))

    ng = 10 ** 9
    ok = 0
    # X以上を使う！と決めるとX以上の個数が自明にわかる。
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if getCount(mid):
            ok = mid
        else:
            ng = mid

    # M個以上あることがわかれば、Mよりも余分な数(同じ値が複数ある場合)
    # はすべてXである事がわかるため、差分だけ引けば良い。
    B = [0] + list(accumulate(A))
    ans = 0
    cnt = 0
    for i in range(N):
        idx = bisect_left(A, ok - A[i])
        ans += B[N] - B[idx] + A[i] * (N - idx)
        cnt += N - idx

    rest = (cnt - M) * ok
    print((ans - rest))


def __starting_point():
    resolve()


__starting_point()
