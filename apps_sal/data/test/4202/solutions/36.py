#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-10 18:36:43 +0900
# LastModified: 2020-09-11 02:01:32 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    L, R = list(map(int, input().split()))
    cool = R // 2019 - L // 2019
    if cool == 0:
        ans = 2020
        for l in range(L, R+1):
            for r in range(l+1, R+1):
                if ans > l*r % 2019:
                    ans = l*r % 2019
        print(ans)

    else:
        print((0))


def __starting_point():
    main()

__starting_point()
