"""input
3
5 2
BGGGG
5 3
RBRGR
5 5
BBBRR
"""
import sys
from collections import defaultdict as dd
mod = 10 ** 9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


for _ in range(int(input())):
    (n, k) = ri()
    a = input()
    rgb = [0 for i in range(n)]
    gbr = [0 for i in range(n)]
    brg = [0 for i in range(n)]
    for i in range(n):
        if i % 3 == 0:
            if a[i] != 'R':
                rgb[i] += 1
        if i % 3 == 1:
            if a[i] != 'G':
                rgb[i] += 1
        if i % 3 == 2:
            if a[i] != 'B':
                rgb[i] += 1
    for i in range(n):
        if i % 3 == 0:
            if a[i] != 'G':
                gbr[i] += 1
        if i % 3 == 1:
            if a[i] != 'B':
                gbr[i] += 1
        if i % 3 == 2:
            if a[i] != 'R':
                gbr[i] += 1
    for i in range(n):
        if i % 3 == 0:
            if a[i] != 'B':
                brg[i] += 1
        if i % 3 == 1:
            if a[i] != 'R':
                brg[i] += 1
        if i % 3 == 2:
            if a[i] != 'G':
                brg[i] += 1
    for i in range(1, n):
        rgb[i] += rgb[i - 1]
        brg[i] += brg[i - 1]
        gbr[i] += gbr[i - 1]
    ans = 999999999
    for i in range(k - 1, n):
        if i - k == -1:
            ans = min(ans, rgb[i], gbr[i], brg[i])
        else:
            ans = min(ans, rgb[i] - rgb[i - k], gbr[i] - gbr[i - k], brg[i] - brg[i - k])
    print(ans)
