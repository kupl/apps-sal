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
    (X, A, B) = LI()
    if B <= A:
        print('delicious')
    elif A < B <= A + X:
        print('safe')
    else:
        print('dangerous')


def __starting_point():
    resolve()


__starting_point()
