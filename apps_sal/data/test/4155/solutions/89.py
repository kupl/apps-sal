import sys
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inl():
    return [int(x) for x in sys.stdin.readline().split()]


def ins():
    return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print('\x1b[33m', *a, '\x1b[0m', **dict(file=sys.stderr, **kw))


def solve():
    n = ini()
    H = inl()

    def calc(l, r, b):
        if l >= r:
            return 0
        mh = min(H[l:r])
        if mh < b:
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
