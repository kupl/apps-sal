from sys import stdin, stdout
from bisect import bisect_left, bisect_right
from collections import defaultdict
import math
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


def find_lt(a, x):  # 'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i - 1]
    raise ValueError


def find_gt(a, x):  # 'Find leftmost value greater than x'
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

# ---------------------Template ends-------------sdpt,sdpt131[Sudipta Banik]---------------------


n, d = readline()
a = readlist()

mp = {}
for i in range(n):
    left = a[i] - d
    right = a[i] + d
    if (i == 0):
        mp[left] = 1
    else:
        if abs(left - a[i - 1]) >= d:
            mp[left] = 1
        else:
            pass

    if i == n - 1:
        mp[right] = 1
    else:
        if(abs(right - a[i + 1])) >= d:
            mp[right] = 1
        else:
            pass
print(len(mp))
