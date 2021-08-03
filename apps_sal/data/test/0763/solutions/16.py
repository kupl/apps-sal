from sys import stdin, stdout
from math import *
from heapq import *
from collections import *


def main():
    n = int(stdin.readline())
    a = [0] + [int(x) for x in stdin.readline().split()]
    res = 1
    minc = 99999999999999999999999999999
    for x in range(1, n + 1):
        c = 0
        for i in range(1, n + 1):
            c = c + (a[i] * (abs(i - x) + abs(i - 1) + abs(1 - x) + abs(x - 1) + abs(1 - i) + abs(i - x)))
        if (c < minc):
            res = x
            minc = c
    stdout.write(str(minc))
    return 0


def __starting_point():
    main()


__starting_point()
