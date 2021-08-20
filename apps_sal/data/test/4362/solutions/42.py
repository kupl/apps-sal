import sys
import os.path
sys.setrecursionlimit(10 ** 5)


def mod():
    return 10 ** 9 + 7


def i():
    return sys.stdin.readline().strip()


def ii():
    return int(sys.stdin.readline())


def li():
    return list(sys.stdin.readline().strip())


def mii():
    return map(int, sys.stdin.readline().split())


def lii():
    return list(map(int, sys.stdin.readline().strip().split()))


def solve():
    a = i()
    if a.isupper():
        print('A')
    else:
        print('a')


for _ in range(1):
    solve()
