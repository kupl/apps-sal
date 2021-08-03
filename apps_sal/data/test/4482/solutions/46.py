import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    a = inl()
    s = sum(a)
    m1 = s // n
    m2 = (s + n - 1) // n

    s1 = sum((x - m1) ** 2 for x in a)
    s2 = sum((x - m2) ** 2 for x in a)
    return min(s1, s2)


print(solve())
