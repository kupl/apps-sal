import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def meguru_bisect(ok, ng):
        """
        is_okを定義して下さい
        :param ok: 取りうる最小の値-1
        :param ng: 取りうる最大の値+1
        :return: is_okを満たす最小(もしくは最大)の値
        """
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok(x):
        cnt = 0
        for h in H:
            h -= b * x
            if h > 0:
                cnt += (h + ab - 1) // ab
        return cnt <= x

    n, a, b = list(map(int, input().split()))
    ab = a - b
    H = list(int(input()) for _ in range(n))

    res = meguru_bisect(10 ** 9 + 1, 0)
    print(res)


def __starting_point():
    resolve()

__starting_point()
