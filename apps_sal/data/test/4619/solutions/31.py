#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-10-09 21:12:23 +0900
# LastModified: 2020-10-09 21:32:50 +0900
#


import os
import sys
import numpy as np
# import pandas as pd


def main():
    W, H, N = list(map(int, input().split()))
    square = [[0, W], [0, H]]
    for _ in range(N):
        x, y, a = list(map(int, input().split()))
        if a == 1 and square[0][0] < x:
            square[0][0] = x

        elif a == 2 and square[0][1] > x:
            square[0][1] = x

        elif a == 3 and square[1][0] < y:
            square[1][0] = y

        elif a == 4 and square[1][1] > y:
            square[1][1] = y

    if square[0][0] >= square[0][1] or \
            square[1][0] >= square[1][1]:
        print((0))
        return
    print(((square[0][1]-square[0][0])*(square[1][1]-square[1][0])))


def __starting_point():
    main()

__starting_point()
