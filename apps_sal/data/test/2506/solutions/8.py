import sys
from bisect import bisect_right, bisect_left
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def meguru_bisect(ok, ng):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(x):
        cnt = 0
        for a in A:
            t = x - a
            idx = bisect_right(A, t)
            cnt += n - idx
        return cnt < m

    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    ng, ok = 0, 10 ** 15 + 1
    mth = meguru_bisect(ok, ng)
    R = [0] + list(accumulate(A))

    res = 0
    cnt = 0
    for a in A:
        s = mth - a
        left = bisect_left(A, s)
        res += (n - left) * a + R[-1] - R[left]
        cnt += n - left
    print((res - mth * (cnt - m)))


def __starting_point():
    resolve()

__starting_point()
