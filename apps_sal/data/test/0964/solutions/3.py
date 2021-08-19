#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time


def flag(a, b, c, d, e, f, X, Y, Z):
    if (b == d and d == f and a + c + e == b):

        m = [[0 for i in range(b)] for i in range(b)]

        for i in range(a):
            for j in range(b):
                m[i][j] = X

        for i in range(a, a + c):
            for j in range(b):
                m[i][j] = Y

        for i in range(a + c, a + c + e):
            for j in range(b):
                m[i][j] = Z

        return (b, m)
    return False


def frame(a, b, c, d, e, f, X, Y, Z):
    if ((a == c + e) and (a == b + d) and (d == f)):

        m = [[0 for i in range(a)] for i in range(a)]

        for i in range(a):
            for j in range(b):
                m[i][j] = X

        for i in range(c):
            for j in range(b, a):
                m[i][j] = Y

        for i in range(c, a):
            for j in range(b, a):
                m[i][j] = Z
        return (a, m)
    return False


def test0(a, b, c, d, e, f, X, Y, Z):
    ans = flag(a, b, c, d, e, f, X, Y, Z)
    if ans == False:
        ans = frame(a, b, c, d, e, f, X, Y, Z)
    return ans


def test(a, b, c, d, e, f, X, Y, Z):
    ans = test0(a, b, c, d, e, f, X, Y, Z)

    if ans == False:
        ans = test0(a, b, c, d, f, e, X, Y, Z)
    if ans == False:
        ans = test0(a, b, d, c, e, f, X, Y, Z)
    if ans == False:
        ans = test0(b, a, c, d, e, f, X, Y, Z)

    if ans == False:
        ans = test0(a, b, d, c, f, e, X, Y, Z)
    if ans == False:
        ans = test0(b, a, c, d, f, e, X, Y, Z)
    if ans == False:
        ans = test0(b, a, d, c, e, f, X, Y, Z)

    if ans == False:
        ans = test0(b, a, d, c, f, e, X, Y, Z)

    return ans


(a, b, c, d, e, f) = (int(i) for i in input().split())

start = time.time()

ans = test(a, b, c, d, e, f, 'A', 'B', 'C')

if ans == False:
    ans = test(c, d, a, b, e, f, 'B', 'A', 'C')

if ans == False:
    ans = test(e, f, a, b, c, d, 'C', 'A', 'B')

if ans == False:
    print(-1)
else:
    print(ans[0])

    for i in range(ans[0]):
        for j in range(ans[0]):
            print(ans[1][i][j], end='')
        print()

finish = time.time()
#print(finish - start)
