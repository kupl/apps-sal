#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-10-01 02:02:04 +0900
# LastModified: 2020-10-01 02:04:56 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    K, S = list(map(int, input().split()))
    ans = 0
    for x in range(K+1):
        for y in range(K+1):
            if 0 <= S - x - y <= K:
                ans += 1
    print(ans)



def __starting_point():
    main()

__starting_point()
