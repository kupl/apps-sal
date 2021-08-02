from sys import stdin, stdout
from math import *
from heapq import *
from collections import *


def main():
    n, k, m = [int(x) for x in stdin.readline().split()]
    a = [int(x) for x in stdin.readline().split()]
    a.sort(reverse=True)
    s = [0] * (n + 2)
    a = [0] + a
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]
    res = s[n] / n
    i = n
    while(i >= 1):
        if (m < 0):
            break
        res = max(res, ((s[i] + min((k * i), m)) / i))
        m = m - 1
        i = i - 1
    stdout.write("%.9f" % (res))
    return 0


def __starting_point():
    main()


__starting_point()
