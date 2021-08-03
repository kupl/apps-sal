from math import *


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


def r3(t):
    return [t(i) for i in input()]


for _ in range(r1(int)):
    n, m = r2(int)
    a = []
    for i in range(n):
        a.append(r2(int))

    c = 0
    for i in range(n):
        if sum(a[i]) > 0:
            c += 1

    c2 = 0
    for j in range(m):
        for i in range(n):
            if a[i][j] > 0:
                c2 += 1
                break

    if min(n - c, m - c2) % 2 == 1:
        print('Ashish')
    else:
        print('Vivek')
