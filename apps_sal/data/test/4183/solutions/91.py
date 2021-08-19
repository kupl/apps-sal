#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-04 15:32:03 +0900
# LastModified: 2020-09-04 15:43:28 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def gcd(a, b):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b


def main():
    n = int(input())
    ans = int(input())
    for _ in range(n - 1):
        t = int(input())
        ans = ans * t // gcd(max(ans, t), min(ans, t))
    print(ans)


def __starting_point():
    main()


__starting_point()
