import sys
import math
from decimal import *


def I():
    return int(sys.stdin.readline())


def IL():
    return list(map(int, sys.stdin.readline().strip().split()))


def ILS():
    return list(map(str, sys.stdin.readline().strip().split()))


def findinv(l):
    p = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                p.append((i, -1 * l[j], j))
    return p


def check(pp):
    for i in range(1, len(pp)):
        if pp[i] < pp[i - 1]:
            return False
    return True


def solve():
    n = I()
    a = IL()
    b = a.copy()
    b.sort()
    inv = []
    for i in range(n):
        inv.append([])
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[j] < a[i]:
                total += 1
                inv[i].append([-1 * a[j], -1 * j])
    for i in range(n):
        inv[i].sort()
    for i in range(n):
        for j in range(len(inv[i])):
            inv[i][j][0] *= -1
            inv[i][j][1] *= -1
    for i in range(n):
        for j in range(len(inv[i])):
            tmp = a[inv[i][j][1]]
            a[inv[i][j][1]] = a[i]
            a[i] = tmp
    flag = 1
    for i in range(n):
        if b[i] != a[i]:
            flag = 0
    if flag == 0:
        print(-1)
    else:
        print(total)
        for i in range(n):
            for j in range(len(inv[i])):
                print(i + 1, inv[i][j][1] + 1)


solve()
