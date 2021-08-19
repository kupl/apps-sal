import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def main():
    n = mint()
    a = [None] * n
    r = [None] * n
    j = 0
    for i in mints():
        a[j] = (n - i, j)
        j += 1
    a.sort()
    j = 1
    i = 0
    while i < n:
        cnt = a[i][0]
        for k in range(i, i + cnt):
            if k >= n or a[k][0] != cnt:
                print('Impossible')
                return
            r[a[k][1]] = j
        j += 1
        i += cnt
    print('Possible')
    print(*r)


main()
