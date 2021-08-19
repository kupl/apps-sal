import sys


def S():
    return sys.stdin.readline().rstrip()


def I():
    return int(sys.stdin.readline().rstrip())


def MI():
    return map(int, sys.stdin.readline().rstrip().split())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def LS():
    return list(sys.stdin.readline().rstrip().split())


(a, b) = MI()
print((a + b) // 2, (a - b) // 2)
