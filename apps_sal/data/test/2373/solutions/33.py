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
    p = [x - 1 for x in inl()]
    cnt = 0
    i = 0
    while i < n:
        if i != p[i]:
            i += 1
        elif i + 1 < n and i + 1 == p[i + 1]:
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    return cnt


print(solve())
