import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    S = ins()
    a = int(S[:2])
    b = int(S[2:])
    am = 0 < a < 13
    bm = 0 < b < 13
    if am and bm:
        return "AMBIGUOUS"
    elif am:
        return "MMYY"
    elif bm:
        return "YYMM"
    else:
        return "NA"


print(solve())
