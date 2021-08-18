import bisect
from collections import defaultdict
import sys
from functools import reduce, cmp_to_key
from collections import deque
import threading
from itertools import combinations


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def rlinput():
    return list(rinput())


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def __starting_point():
    for _ in range(iinput()):
        a, b, c, d = rinput()
        print(b, c, c)


__starting_point()
