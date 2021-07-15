#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-12-05 14:11:23 +0900
# LastModified: 2020-12-05 14:40:12 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    x = int(input())
    if x % 11 == 0:
        print((2*(x//11)))
        return
    tmp = x // 11
    ans = tmp*2
    new = x - tmp*11
    if 0 < new <= 6:
        print((ans+1))
    else:
        print((ans+2))








def __starting_point():
    main()

__starting_point()
