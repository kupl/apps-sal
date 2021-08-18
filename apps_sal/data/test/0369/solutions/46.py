import sys
sys.setrecursionlimit(10**6)
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62 - 1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


class Mod:
    def __init__(self, m):
        self.m = m

    def add(self, a, b):
        return (a + b) % self.m

    def sub(self, a, b):
        return (a - b) % self.m

    def mul(self, a, b):
        return ((a % self.m) * (b % self.m)) % self.m

    def div(self, a, b):
        return self.mul(a, pow(b, self.m - 2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)


class Bisect:
    def __init__(self, func):
        self.__func = func

    def bisect_left(self, x, lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if self.__func(mid) < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def bisect_right(self, x, lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if x < self.__func(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


@mt
def slv(N, M, S):

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(x):
        if x == 0:
            return []

        for i in range(M, 0, -1):
            if 0 <= x - i and S[x - i] == '0':
                r = dfs(x - i)
                if r is not None:
                    r.append(i)
                    return r
        return None
    ans = dfs(N)
    if ans is None:
        ans = [-1]
    return ans


def main():
    N, M = read_int_n()
    S = read_str()
    print(*slv(N, M, S))


def __starting_point():
    main()


__starting_point()
