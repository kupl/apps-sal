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
    n = I()
    if n % 2 == 0:
        ans = 0
        for i in range(1, 27):
            ans += n // (2 * pow(5, i))
        print(ans)
    else:
        print(0)


main()
