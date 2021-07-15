# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys

"""
created by shhuan at 2018/11/24 15:29

"""

T = int(input())


def interact(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    ans = (-1, -1, -1, -1)
    if x2 < x3 or x4 < x1:
        return 0, ans
    if y2 < y3 or y4 < y1:
        return 0, ans

    ans = (max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4))

    return area(ans), ans


def area(rect):
    return (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)


def winrect(rect):
    a = area(rect)
    if a % 2 == 0:
        return a // 2

    x1, y1, x2, y2 = rect
    e1, e2 = x1 % 2 == 0, y1 % 2 == 0
    ow = (e1 and e2) or (not e1 and not e2)
    return a // 2 + 1 if ow else a // 2

ans = []
for ti in range(T):
    N, M = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    w = winrect((1, 1, N, M))
    a, b = (x1, y1, x2, y2), (x3, y3, x4, y4)
    s, c = interact(a, b)
    if s == 0:
        w -= winrect(a) + winrect(b)
        w += area(a)
    elif s == area(a):
        w -= winrect(b)
    elif s == area(b):
        w -= winrect(b)
        w += area(a) - area(b) - (winrect(a) - winrect(b))
    else:
        w += area(a) - winrect(a)
        w -= winrect(b)
        w -= area(c) - winrect(c)

    ans.append((w, N*M-w))

print('\n'.join(['{} {}'.format(a, b) for a, b in ans]))
