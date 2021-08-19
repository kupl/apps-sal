import sys
import math
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
N = ini()
if N <= 999:
    print('ABC')
else:
    print('ABD')
