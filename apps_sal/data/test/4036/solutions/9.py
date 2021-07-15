#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import math
"""
26 6
2 5


"""


def solution():
    n, k = list(map(int, input().strip().split()))
    # n, k = 200, 30

    a = []
    for i in range(k):
        mi = math.floor((2 * n / (k - i) + i + 1 - k) / 2)
        if mi < 0:
            break
        mi = 2 * a[-1] if len(a) > 0 and mi > 2 * a[-1] else mi
        a.append(mi)
        n -= mi

    if n != 0:
        print('NO')
        # print(a)
    else:
        print('YES')
        print(' '.join(map(str, a)))
        # print(sum(a))


while True:
    try:
        solution()

    except:
        break
# solution()

