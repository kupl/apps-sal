#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-10-03 20:05:16 +0900
# LastModified: 2020-10-03 20:28:14 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    S = input()
    stack = []
    for s in S:
        if s == '0' or s == '1':
            stack.append(s)
        elif s == 'B' and stack:
            stack.pop()
    for sta in stack:
        print(sta, end="")
    print()


def __starting_point():
    main()


__starting_point()
