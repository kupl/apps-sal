import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inl(): return [int(x) for x in sys.stdin.readline().split()]
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    a, b = inl()
    a = (a + 11) % 13
    b = (b + 11) % 13
    if a == b:
        return "Draw"
    elif a > b:
        return "Alice"
    return "Bob"


print(solve())
