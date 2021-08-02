import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    p = [x - 1 for x in inl()]
    cnt = 0
    i = 0
    while i < n:
        if i != p[i]:
            i += 1
        elif i + 1 < n and (i + 1) == p[i + 1]:
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1

    return cnt


print(solve())
