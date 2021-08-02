from sys import stdin
import functools
import math


def read(): return list(map(int, stdin.readline().split()))


n, m = read()

b = min(n, m)
a = n + m - 1 - b
print("{0} {1}".format(a, b))
