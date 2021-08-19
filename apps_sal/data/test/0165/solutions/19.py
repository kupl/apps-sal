from collections import defaultdict
import sys
import os
import math


def __starting_point():
    #n, m = list(map(int, input().split()))
    b, d, s = map(int, input().split())
    ans = 0
    if b > d and b > s:
        ans = (b - 1) * 3 + 1 - d - b - s
    elif d > b and d > s:
        ans = (d - 2) * 3 + 4 - d - b - s
    elif s > d and s > b:
        ans = (s - 1) * 3 + 1 - d - b - s
    elif s == d == b:
        ans = 0
    elif d == b:
        ans = (b - 1) * 3 + 2 - d - b - s
    elif b == s:
        ans = (b - 1) * 3 + 2 - d - b - s
    else:
        ans = (d - 1) * 3 + 2 - d - b - s
    print(ans)


__starting_point()
