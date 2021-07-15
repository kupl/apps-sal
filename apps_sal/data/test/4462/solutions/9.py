#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-04 15:44:42 +0900
# LastModified: 2020-09-13 16:06:20 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    A = list(map(int, input().split()))
    A_4 = [x for x in A if x % 4 == 0]
    A_2 = [x for x in A if x % 4 != 0 and x % 2 == 0]
    A_0 = [x for x in A if x % 2 != 0]
    if len(A_2) == 0 and len(A_0) <= len(A_4) + 1:
        print("Yes")
    elif len(A_0) <= len(A_4):
        print("Yes")
    else:
        print("No")

def __starting_point():
    main()

__starting_point()
