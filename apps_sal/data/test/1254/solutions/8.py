from sys import stdin, stdout
from math import *
from heapq import *
from collections import *


def inputlistint():
    return [int(x) for x in stdin.readline().split()]


def main():
    n, m = inputlistint()
    s = []
    r = []
    f = []
    for _ in range(m + 2):
        f.append([])
    for _ in range(n):
        a, b = inputlistint()
        s.append(a)
        r.append(b)
        f[a].append(b)
    f.sort(key=lambda x: len(x), reverse=True)
    for a in f:
        a.sort(reverse=True)
    res = 0
    for k in range(len(f[0])):
        test = 0
        for i in range(m + 1):
            if (k >= len(f[i])):
                break
            if (k > 0):
                f[i][k] = f[i][k] + f[i][k - 1]
            if (f[i][k] > 0):
                test = test + f[i][k]
        res = max(res, test)
    stdout.write(str(res))
    return 0


def __starting_point():
    main()


__starting_point()
