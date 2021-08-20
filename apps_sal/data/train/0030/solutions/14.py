import sys


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c for j in range(b)] for i in range(a)]


def list3d(a, b, c, d):
    return [[[d for k in range(c)] for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e for l in range(d)] for k in range(c)] for j in range(b)] for i in range(a)]


def ceil(x, y=1):
    return int(-(-x // y))


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST(N=None):
    return list(MAP()) if N is None else [INT() for i in range(N)]


def Yes():
    print('Yes')


def No():
    print('No')


def YES():
    print('YES')


def NO():
    print('NO')


INF = 10 ** 19
MOD = 10 ** 9 + 7
EPS = 10 ** (-10)


def RLE(data):
    from itertools import groupby
    return [(x, len(list(grp))) for (x, grp) in groupby(data)]


def check(S, T):
    A = [0] * N
    for i in range(N):
        if S[i] != T[i]:
            A[i] = 1
    rle = RLE(A)
    cnt = 0
    for (x, _) in rle:
        if x:
            cnt += 1
    return cnt


for _ in range(INT()):
    N = INT()
    S = input()
    T1 = '01' * (N // 2)
    T2 = '10' * (N // 2)
    ans = min(check(S, T1), check(S, T2))
    print(ans)
