from collections import defaultdict
import sys
import os
import math


def __starting_point():
    n, b, d = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt, sm = 0, 0
    for i in arr:
        if i > b:
            continue
        sm += i
        if sm > d:
            sm = 0
            cnt += 1
    print(cnt)


__starting_point()
