#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy
# sys.setrecursionlimit(1000000)

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def next(su, ai, sign):
    assert sign in [-1, 1]
    if (su + ai) * sign > 0:
        return ai
    else:
        nextsu = sign
        nextai = nextsu - su
        return nextai

def main():
    n = int(input())
    an = list(map(int, input().split()))

    ress = HUGEL
    for beg in [-1, 1]:
        res = 0
        su = 0
        sign = beg
        for i in range(n):
            ai = next(su, an[i], sign)
            su = su + ai
            res += abs(ai - an[i])
            sign *= (-1)
        ress = min(ress, res)

    print(ress)

main()

