#import math
#import itertools
#import numpy as np
from collections import deque


def INT(): return int(input())
def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())
def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    n, k = INTM()
    d = LIST()
    # q=deque(d)
    nkmin = min(n, k)
    stop = 10**9
    ans = 0
    for i1 in range(1, 1 + nkmin):
        for i2 in range(i1 + 1):
            temp = d[0:i2] + d[n - (i1 - i2):]
            # print(temp,i1,i2)
            temp = sorted(temp)
            # print(temp,i1,i2)
            for i3 in range(i1):
                if temp[i3] >= 0 or i3 >= k - i1:
                    stop = i3
                    break
                stop = 10**9
            if stop != 10**9:
                # print(temp[i3:],1)
                ans = max(sum(temp[i3:]), ans)

    print(ans)


def __starting_point():
    do()


__starting_point()
