#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B_fix2
# CreatedDate:  2020-11-21 21:26:09 +0900
# LastModified: 2020-12-04 15:29:40 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N = int(input())
    S = input()
    T = ""
    for s in S:
        T += s
        if len(T) >= 3 and T[-3:] == "fox":
            T = T[:-3]
    print((len(T)))


def __starting_point():
    main()


__starting_point()
