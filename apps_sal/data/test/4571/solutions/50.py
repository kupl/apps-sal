#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-27 01:33:17 +0900
# LastModified: 2020-10-09 16:05:14 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N, M = list(map(int, input().split()))
    para0 = (1900 * M + 100 * (N - M)) / (2**M)
    para1 = 1 - (1 / (2**M))
    para0_ = para0
    para1_ = 1 / ((1 - para1)**2)
    print((int(para0_ * para1_)))


def __starting_point():
    main()


__starting_point()
