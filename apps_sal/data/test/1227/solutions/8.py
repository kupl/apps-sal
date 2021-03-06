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
N = ins()
K = ini()


def solve():
    M = len(N)
    dp_eq = [[0 for _ in range(K + 1)] for _ in range(M)]
    dp_less = [[0 for _ in range(K + 1)] for _ in range(M)]
    dp_eq[0][K - 1] = 1
    dp_less[0][K] = 1
    dp_less[0][K - 1] = ord(N[0]) - ord('0') - 1
    for i in range(1, M):
        is_zero = N[i] == '0'
        for k in range(K + 1):
            if is_zero:
                dp_eq[i][k] = dp_eq[i - 1][k]
            elif k < K:
                dp_eq[i][k] = dp_eq[i - 1][k + 1]
            dp_less[i][k] = dp_less[i - 1][k]
            if k < K:
                dp_less[i][k] += dp_less[i - 1][k + 1] * 9
            if not is_zero:
                dp_less[i][k] += dp_eq[i - 1][k]
                if k < K:
                    dp_less[i][k] += dp_eq[i - 1][k + 1] * (ord(N[i]) - ord('0') - 1)
    return dp_eq[M - 1][0] + dp_less[M - 1][0]


print(solve())
