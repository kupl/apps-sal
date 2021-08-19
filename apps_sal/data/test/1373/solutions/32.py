import bisect
import collections
import copy
import itertools
import math
import string
import sys


def I():
    return int(sys.stdin.readline().rstrip())


def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def S():
    return sys.stdin.readline().rstrip()


def LS():
    return list(sys.stdin.readline().rstrip().split())


def main():
    (n, k) = LI()
    N = 10 ** 9 + 7
    ans = 0
    start = sum([i for i in range(0, k - 1)])
    goal = sum([i for i in range(n, n - k + 1, -1)])
    for (i, j) in zip(range(k - 1, n + 1), range(n - k + 1, -1, -1)):
        start += i
        goal += j
        cnt = (goal - start + 1) % N
        ans += cnt
        ans %= N
    print(ans)


main()
