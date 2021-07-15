#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-10-03 20:30:05 +0900
# LastModified: 2020-10-03 20:50:25 +0900
#


import os
import sys
import numpy as np
# import pandas as pd


def main():
    N, K = list(map(int, input().split()))
    A = np.array(list(map(int, input().split())))
    cnt = 0
    i = 0
    while i != N-1:
        if i == 0:
            A[i: i+K] = np.min(A[i: i+K])
            cnt += 1
            i = i+K-1

        elif i+K < N:
            A[i: i+K] = A[i]
            cnt += 1
            i = i+K-1

        else:
            A[i: -1] = A[i]
            cnt += 1
            break

    print(cnt)







def __starting_point():
    main()

__starting_point()
