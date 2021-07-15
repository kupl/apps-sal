#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix
# CreatedDate:  2020-10-10 15:17:07 +0900
# LastModified: 2020-10-10 15:25:36 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from itertools import accumulate


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_ac = list(accumulate(A))
    ans = A_ac[-1]
    for i, ac in enumerate(A_ac):
        if i == 0:
            ans = abs(2*ac-A_ac[-1])
        if i == N-1:
            break
        if abs(2*ac-A_ac[-1]) < ans:
            ans = abs(2*ac-A_ac[-1])
    print(ans)



def __starting_point():
    main()

__starting_point()
