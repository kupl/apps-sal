from bisect import bisect, bisect_left


class BisectSearch:
    @staticmethod
    def search_float(f, l=0, r=10**9, epsilon=1e-9, return_left=False):
        assert f(l) and (not f(r))
        while r - l > epsilon:
            m = (r + l) / 2
            if f(m):
                l = m
            else:
                r = m
        if return_left:
            return l
        return r

    @staticmethod
    def search_int(f, l=0, r=10**9, return_left=False):
        assert f(l) and (not f(r))
        while r - l > 1:
            m = (r + l) // 2
            if f(m):
                l = m
            else:
                r = m
        if return_left:
            return l
        return r

    @staticmethod
    def search_list(key, A, return_left=False):
        search = bisect_left if return_left else bisect
        return search(A, key)


def arithmetic_series(n, d=1, a=1):
    return n * (2 * a + (n - 1) * d) // 2


n = int(input())
bs = BisectSearch


def f(x):
    return arithmetic_series(x) <= n + 1


print(n + 1 - bs.search_int(f, l=1, r=n + 1, return_left=True))
