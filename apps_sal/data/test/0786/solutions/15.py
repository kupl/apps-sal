from collections import defaultdict
import sys
import os
import math


def __starting_point():
    n = int(input())
    (l, r) = (-200000000, 200000000)
    temp = 0
    for i in range(n):
        (a, b) = map(int, input().split())
        if b == 1:
            l = max(1900 - temp, l)
        else:
            r = min(1900 - temp, r)
        temp += a
    if r == 200000000:
        print('Infinity')
    elif l >= r:
        print('Impossible')
    else:
        print(temp + r - 1)


__starting_point()
