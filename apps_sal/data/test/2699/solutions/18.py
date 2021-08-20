import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
sys.setrecursionlimit(100000000)


def ii():
    return int(input())


def si():
    return input()


def jn(x, l):
    return x.join(map(str, l))


def sl():
    return list(map(str, input().strip()))


def mi():
    return map(int, input().split())


def mif():
    return map(float, input().split())


def lii():
    return list(map(int, input().split()))


def ceil(x):
    return int(x) if x == int(x) else int(x) + 1


def ceildiv(x, d):
    return x // d if x % d == 0 else x // d + 1


def flush():
    return stdout.flush()


def stdstr():
    return stdin.readline()


def stdint():
    return int(stdin.readline())


def stdpr(x):
    return stdout.write(str(x))


mod = 1000000007
n = ii()
arr = lii()
for i in range(n):
    for j in range(4):
        if j == 0:
            val = 1
        elif j == 1:
            val = 2
        elif j == 2:
            val = 4
        elif j == 3:
            val = 3
        for k in range(arr[i]):
            ans = 0
            if k > 0:
                ans = 2 ** (k - 1)
            if j == 3:
                val += 3 * ans
                print(val, end=' ')
            elif j == 0 or j == 1:
                val += 3 * ans
                print(val, end=' ')
            else:
                val += 6 * ans
                print(val, end=' ')
        print()
