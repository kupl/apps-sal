#                                               |
#   _` |  __ \    _` |   __|   _ \   __ \    _` |   _` |
#  (   |  |   |  (   |  (     (   |  |   |  (   |  (   |
# \__,_| _|  _| \__,_| \___| \___/  _|  _| \__,_| \__,_|

import sys
import math


def read_line():
    return sys.stdin.readline()[:-1]


def read_int():
    return int(sys.stdin.readline())


def read_int_line():
    return [int(v) for v in sys.stdin.readline().split()]


def read_float_line():
    return [float(v) for v in sys.stdin.readline().split()]


t = read_int()
for i in range(t):
    n = read_int()
    a = read_int_line()
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]].append(i)
        else:
            d[a[i]] = [i]

    dp = [1] * len(list(d.keys()))

    s = list(d.keys())
    s.sort()

    for i in range(len(s) - 2, -1, -1):
        if d[s[i]][-1] < d[s[i + 1]][0]:
            dp[i] = dp[i + 1] + 1
        else:
            dp[i] = 1
    ans = len(s) - max(dp)
    print(ans)
