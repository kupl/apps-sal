from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import bisect
import sys
sys.setrecursionlimit(10000000)
mod = 10 ** 9 + 7
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


(a, b, x) = readInts()
ok = 0
ng = 10 ** 9 + 1


def is_ok(mid):
    if a * mid + b * len(str(mid)) <= x:
        return True
    else:
        return False


while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
