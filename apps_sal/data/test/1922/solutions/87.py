#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix
# CreatedDate:  2020-10-01 22:03:15 +0900
# LastModified: 2020-10-01 22:18:35 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N, M = list(map(int, input().split()))
    if N >= 2 and M >= 2:
        print(((N-2)*(M-2)))
    elif N < 2 and M >= 2:
        print((M-2))
    elif N >= 2 and M < 2:
        print((N-2))
    else:
        print((1))


def __starting_point():
    main()

__starting_point()
