#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-27 00:00:39 +0900
# LastModified: 2020-09-27 00:16:46 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N, M = list(map(int, input().split()))
    path = []
    for _ in range(N):
        A, B = list(map(int, input().split()))
        path.append([A, B])
    path.sort(key=lambda x: x[0])
#    print(path)
    ans = [0, 0]  # (much, num)
    for p in path:
        if ans[1] + p[1] <= M:
            ans[0] = ans[0] + p[0] * p[1]
            ans[1] += p[1]

        else:
            num = M - ans[1]
            ans[0] = ans[0] + p[0] * num
            ans[1] = ans[1] + num
        if ans[1] == M:
            print((ans[0]))
            return
#        print(ans)


def __starting_point():
    main()


__starting_point()
