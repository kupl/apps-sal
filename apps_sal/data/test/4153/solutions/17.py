#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-11 14:10:37 +0900
# LastModified: 2020-09-11 14:16:43 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    S = input()
    if S.count('0') < S.count('1'):
        print((S.count('0') * 2))
    else:
        print((S.count('1') * 2))


def __starting_point():
    main()


__starting_point()
