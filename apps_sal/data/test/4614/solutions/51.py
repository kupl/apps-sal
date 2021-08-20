import sys
import collections


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
    ABC = LI()
    cnt = collections.Counter(ABC)
    ans = [k for (k, v) in list(cnt.items()) if v == 1]
    print(ans[0])


def __starting_point():
    resolve()


__starting_point()
