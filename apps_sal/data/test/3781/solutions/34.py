import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    a = inl()
    if n % 2 == 1:
        return "Second"
    a.sort()
    pair_ok = True
    i = 0
    while i < n:
        if a[i] != a[i + 1]:
            pair_ok = False
            break
        i += 2
    if pair_ok:
        return "Second"
    return "First"


T = ini()
for i in range(T):
    print(solve())
