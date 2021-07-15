#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-10-09 21:07:08 +0900
# LastModified: 2020-10-09 21:11:06 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_cnt = Counter(A)
    ans = 0
    for key, value in list(A_cnt.items()):
        if key == value:
            pass
        elif key > value:
            ans += value
        else:
            ans += value-key
    print(ans)


def __starting_point():
    main()

__starting_point()
