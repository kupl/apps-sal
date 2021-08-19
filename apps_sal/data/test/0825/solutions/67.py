from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product
from collections import deque, defaultdict, Counter
import decimal
import re
import math
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


n = I()


def soinsu(n):
    dic = defaultdict(int)
    i = 2
    while i * i <= n:
        if n % i == 0:
            dic[i] += 1
            n //= i
        else:
            i += 1
    if n != 1:
        dic[n] += 1
    return dic


dic = soinsu(n)
ans = 0
for (k, v) in list(dic.items()):
    i = 1
    while True:
        if v >= i:
            ans += 1
            v -= i
            i += 1
        else:
            break
print(ans)
