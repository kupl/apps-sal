import sys
sys.setrecursionlimit(10 ** 8)


def ini():
    return int(sys.stdin.readline())


def inm():
    return list(map(int, sys.stdin.readline().split()))


def inl():
    return list(inm())


def ins():
    return sys.stdin.readline().rstrip()


s = ins()


def solve():
    lreq = s[0] == s[-1]
    odd = len(s) % 2 == 1
    return odd ^ lreq


print('First' if solve() else 'Second')
