import sys


def input():
    return sys.stdin.readline().strip()


def list2d(a, b, c):
    return [[c] * b for i in range(a)]


def list3d(a, b, c, d):
    return [[[d] * c for j in range(b)] for i in range(a)]


def list4d(a, b, c, d, e):
    return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]


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


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7
N = INT()
A = [a * 2 for a in LIST()] + [1]
B = [b * 2 for b in LIST()] + [0]


def check1(i, t):
    nxtt = cur
    for j in range(i + 1, N + 1):
        nxtt += A[j - 1]
        dist = nxtt - t
        if spd + 2 - dist > B[j]:
            return False
    return True


def check2(i, t):
    nxtt = cur
    for j in range(i + 1, N + 1):
        nxtt += A[j - 1]
        dist = nxtt - t
        if spd + 1 - dist > B[j]:
            return False
    return True


cur = spd = sm = 0
for (i, a) in enumerate(A[:N]):
    b = B[i]
    for t in range(cur, cur + a):
        if spd + 1 <= b and check1(i, t):
            sm += spd + 0.5
            spd += 1
        elif spd <= b and check2(i, t):
            sm += spd
        else:
            sm += spd - 0.5
            spd -= 1
    cur += a
print(sm / 4)
