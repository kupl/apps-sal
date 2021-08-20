import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20


def I():
    return int(input())


def F():
    return float(input())


def S():
    return input()


def LI():
    return [int(x) for x in input().split()]


def LI_():
    return [int(x) - 1 for x in input().split()]


def LF():
    return [float(x) for x in input().split()]


def LS():
    return input().split()


def resolve():
    N = I()
    lucas = [0] * (N + 1)
    lucas[0] = 2
    lucas[1] = 1
    for i in range(N - 1):
        lucas[i + 2] = lucas[i] + lucas[i + 1]
    print(lucas[-1])


def __starting_point():
    resolve()


__starting_point()
