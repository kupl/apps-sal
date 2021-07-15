#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	sample
# CreatedDate:  2020-12-28 15:44:13 +0900
# LastModified: 2020-12-28 20:02:31 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N, M = list(map(int, input().split()))
    if N == 1 and M == 1:
        print((1))
    elif (N == 1 and M != 1):
        print((M-2))
    elif (N != 1 and M == 1):
        print((N-2))
    else:
        print(((N-2)*(M-2)))


def __starting_point():
    main()

__starting_point()
