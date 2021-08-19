import sys
import math
import bisect
sys.setrecursionlimit(1000000000)


def input():
    return sys.stdin.readline().strip()


def iinput():
    return int(input())


def finput():
    return float(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def rlinput():
    return list(rinput())


def main():
    n = iinput()
    c = rlinput()
    (q, res, w, e) = ([0] * n, ['0'] * n, 0, n)
    for i in range(n):
        q[c[i] - 1] = i
    for i in range(n):
        w = max(q[i], w)
        e = min(q[i], e)
        if w <= i + e:
            res[i] = '1'
    print(''.join(res))


for j in range(int(input())):
    main()
