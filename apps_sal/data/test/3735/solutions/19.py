from sys import stdin, stdout
from bisect import bisect_left, bisect_right
from collections import defaultdict
import math
from fractions import Fraction as frac
from random import random
cin = stdin.readline


def cout(x):
    stdout.write(str(x) + '\n')


def var(type=int):
    return type(stdin.readline())


def readline(type=int):
    return map(type, stdin.readline().split())


def readlist(type=int):
    return list(map(type, stdin.readline().split()))


def sorted_indexes(arr):
    return sorted(range(len(arr)), key=arr.__getitem__)


def printr(arr):
    [stdout.write(str(x) + ' ') for x in arr]
    cout('')


def find_lt(a, x):
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def dist(x, y):
    return math.sqrt(x * x + y * y)


def binary_search(arr, x):
    i = bisect_left(arr, x)
    if i == len(arr) or arr[i] != x:
        return -1
    return i


MOD2 = 998244353


def sm(x):
    x = str(x)
    s = 0
    for n in x:
        s += int(n)
    return s


n = int(input())
a = 0
a_prev = 0
while a <= n:
    a_prev = a
    a = a * 10 + 9
a = a_prev
print(sm(n - a) + sm(a))
