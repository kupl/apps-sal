import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    a = inl()
    a = [0] + a
    a.append(0)

    total = 0
    for i in range(1, n + 2):
        total += abs(a[i] - a[i - 1])
    for i in range(1, n + 1):
        diff = abs(a[i + 1] - a[i - 1]) - abs(a[i] - a[i - 1]) - abs(a[i + 1] - a[i])
        print(total + diff)


solve()

