from sys import stdin, stdout
from collections import defaultdict
from functools import lru_cache
from math import gcd, floor, ceil


def ilist():
    return [int(x) for x in stdin.readline().strip().split(" ")]


def iint():
    return int(stdin.readline())


def istr():
    return stdin.readline().strip()


s = istr()
print(int(s[-1]) % 2)
