#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-10 18:27:16 +0900
# LastModified: 2020-09-10 18:35:34 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from collections import Counter


def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(int(input()))
    A_cnt = Counter(A)
    flag = 0
    A_max = max(A)
    A_next_max = sorted(A, reverse=True)[1]
    if A_cnt[A_max] > 1:
        flag = 1

    for a in A:
        if a == A_max and flag == 1:
            print(A_max)
        elif a == A_max and flag == 0:
            print(A_next_max)
        else:
            print(A_max)


def __starting_point():
    main()

__starting_point()
