#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D
# CreatedDate:  2020-08-30 13:56:28 +0900
# LastModified: 2020-08-30 14:22:16 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from collections import Counter


def main():
    N, K = list(map(int, input().split()))
    R, S, P = list(map(int, input().split()))
    T = input()
    takahashi = ''
    for t in T:
        if t == 's':
            takahashi += 'r'
        elif t == 'p':
            takahashi += 's'
        else:
            takahashi += 'p'

    for i in range(K, N):
        if takahashi[i-K] == takahashi[i]:
            takahashi = takahashi[:i] + '_' + takahashi[i+1:]
    ans = takahashi.count('r')*R + takahashi.count('s')*S + takahashi.count('p')*P
    print(ans)

def __starting_point():
    main()

__starting_point()
