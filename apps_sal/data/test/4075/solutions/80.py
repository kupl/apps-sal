#import math
import itertools
#import numpy as np
#from collections import deque


INT = lambda: int(input())
INTM = lambda: map(int, input().split())
STRM = lambda: map(str, input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int, input().split()))
LISTS = lambda: list(map(str, input().split()))


def do():
    n, m = INTM()
    cnct = []
    for i in range(m):
        temp = LIST()
        temp = temp[1:]
        cnct.append(temp)
    ps = LIST()
    ans = 0

    for bit in range(2**n):
        check = [0] * m
        for i in range(n):
            if (bit >> i) & 1:
                for k in range(m):
                    if i + 1 in cnct[k]:
                        check[k] += 1

        flg = True
        for k in range(m):
            if check[k] % 2 != ps[k]:
                flg = False

        if flg:
            ans += 1

    print(ans)


def __starting_point():
    do()


__starting_point()
