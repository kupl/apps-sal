#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix
# CreatedDate:  2020-12-29 11:19:58 +0900
# LastModified: 2020-12-29 11:33:43 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A_min = min(A)
    cnt = 0
    for i in range(0, N-1, K-1):
        cnt += 1
    print(cnt)




def __starting_point():
    main()

__starting_point()
