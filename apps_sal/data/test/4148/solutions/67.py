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
    s = ins()
    ans = []
    for c in s:
        x = chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        ans.append(x)
    return ''.join(ans)


print(solve())
