import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    S = ins()
    K = ini()
    ones = 0
    for i, d in enumerate(S):
        if d != "1":
            break
        ones += 1
    if K <= ones:
        return "1"
    return S[ones]


print(solve())

