#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-10-08 14:36:20 +0900
# LastModified: 2020-10-08 14:41:46 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    S = input()
    ans_1 = 0
    ans_2 = 0
    for i, s in enumerate(S):
        if i % 2 == 0 and s == '1':
            ans_1 += 1
        elif i % 2 == 1 and s == '0':
            ans_1 += 1
        if i % 2 == 0 and s == '0':
            ans_2 += 1
        elif i % 2 == 1 and s == '1':
            ans_2 += 1
    print((min(ans_1, ans_2)))


def __starting_point():
    main()


__starting_point()
