#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D
# CreatedDate:  2020-09-03 21:15:23 +0900
# LastModified: 2020-09-03 21:29:19 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    S = []
    for _ in range(n):
        S.append(list(map(int, input().split())))
    S.sort(key=lambda x: x[1])
    current_time = 0
    for s in S:
        current_time += s[0]
        if current_time <= s[1]:
            pass
        else:
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
