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
    return list(map(type, stdin.readline().split()))


def readlist(type=int):
    return list(map(type, stdin.readline().split()))


def sorted_indexes(arr):
    return sorted(list(range(len(arr))), key=arr.__getitem__)


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


(n, a, b) = readline(int)
price = [a, b]
arr = readlist(int)
half = n // 2
cost = 0
flg = True
for i in range(half):
    if arr[i] == arr[n - 1 - i] == 2:
        cost += 2 * min(a, b)
    elif arr[i] == 2 and arr[n - 1 - i] <= 1:
        cost += price[arr[n - 1 - i]]
    elif arr[i] <= 1 and arr[n - 1 - i] == 2:
        cost += price[arr[i]]
    elif arr[i] != arr[n - 1 - i]:
        flg = False
        break
if n % 2 == 1:
    if arr[half] == 2:
        cost += min(a, b)
if not flg:
    print(-1)
else:
    print(cost)
