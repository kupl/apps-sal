import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    s = [ini() for _ in range(n)]
    a = sum(s)
    if a % 10 != 0:
        return a
    m = 1000
    for x in s:
        if x % 10 != 0 and m > x:
            m = x
    if m == 1000:
        return 0
    return a - m


print(solve())

