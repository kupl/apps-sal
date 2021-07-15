#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix
# CreatedDate:  2020-09-03 20:30:23 +0900
# LastModified: 2020-09-03 21:14:03 +0900
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
    a, b, c, d = list(map(int, input().split()))
    if (a/c).is_integer():
        c_cnt = b//c - a//c + 1
#        print(b//c, a//c)
    else:
        c_cnt = b//c - a//c
#        print(b//c, a//c)
    if (a/d).is_integer():
        d_cnt = b//d - a//d + 1
#        print(b//d, a//d)
    else:
        d_cnt = b//d - a//d
#        print(b//d, a//d)

    lcm = c * d // gcd(max(c, d), min(c, d))
    if (a/lcm).is_integer():
        lcm_cnt = b//lcm - a//lcm + 1
    else:
        lcm_cnt = b//lcm - a//lcm
#    print(c_cnt, d_cnt, lcm_cnt)
    print((b-a+1-c_cnt-d_cnt+lcm_cnt))


def __starting_point():
    main()

__starting_point()
