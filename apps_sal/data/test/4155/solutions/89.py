import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inl = lambda: [int(x) for x in sys.stdin.readline().split()]
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    H = inl()

    def calc(l, r, b):
        if l >= r:
            return 0
        mh = min(H[l:r])
        # debug(H[l:r], mh)
        if mh < b:
            # debug(mh, b, l, r)
            return 0
        res = mh - b
        i = l
        while i < r:
            if H[i] == mh:
                res += calc(l, i, mh)
                l = i + 1
            i += 1
        res += calc(l, r, mh)
        return res

    return calc(0, n, 0)


print(solve())

