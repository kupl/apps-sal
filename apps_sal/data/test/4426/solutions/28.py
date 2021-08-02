import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

d = {
    "SAT": 1,
    "FRI": 2,
    "THU": 3,
    "WED": 4,
    "TUE": 5,
    "MON": 6,
    "SUN": 7,
}


def solve():
    S = ins()
    return d[S]


print(solve())
