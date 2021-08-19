import sys
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inm():
    return map(int, sys.stdin.readline().split())


def inl():
    return list(inm())


def ins():
    return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print('\x1b[33m', *a, '\x1b[0m', **dict(file=sys.stderr, **kw))
N = ini()
(A, B) = ([], [])
for i in range(N):
    (a, b) = inm()
    A.append(a)
    B.append(b)


def solve():
    sa = sorted(A)
    sb = sorted(B)
    if N % 2 == 1:
        return sb[N // 2] - sa[N // 2] + 1
    else:
        return sb[N // 2] + sb[N // 2 - 1] - (sa[N // 2] + sa[N // 2 - 1]) + 1


print(solve())
