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


(N, M) = MI()
X = LI()
ANS = set(X[1:])
for i in range(N - 1):
    X = LI()
    ANS &= set(X[1:])
print(len(ANS))
