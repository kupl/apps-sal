
import sys
import io
import math
import collections
import decimal
import itertools
from queue import PriorityQueue
import bisect


def input():
    return sys.stdin.readline()[:-1]


sys.setrecursionlimit(1000000)


def main():
    a = sorted(list(map(int, input().split())))
    if a[0] + a[1] + a[2] == a[3] or a[0] + a[2] == a[1] + a[3] or a[0] + a[3] == a[1] + a[2]:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
