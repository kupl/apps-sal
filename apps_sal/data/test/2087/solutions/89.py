import sys
sys.setrecursionlimit(10 ** 7)


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LI2():
    return list(map(int, sys.stdin.readline().rstrip()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def LS2():
    return list(sys.stdin.readline().rstrip())


(A, B, C) = MI()
mod = 998244353
ans = A * (A + 1) // 2 * B * (B + 1) // 2 * C * (C + 1) // 2
ans %= mod
print(ans)
