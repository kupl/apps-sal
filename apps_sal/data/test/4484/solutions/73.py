import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

MOD = 10 ** 9 + 7


def fac(k):
    res = 1
    for i in range(2, k + 1):
        res = (res * i) % MOD
    return res


def solve():
    n, m = inl()
    if n < m:
        n, m = m, n
    if n - m > 1:
        return 0
    if n - m == 1:
        return fac(n) * fac(m) % MOD
    assert n == m
    a = fac(n)
    a = 2 * a * a % MOD
    return a


print(solve())
