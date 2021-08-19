#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	sample
# CreatedDate:  2020-09-27 14:00:12 +0900
# LastModified: 2020-09-27 14:35:21 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from collections import Counter


def main():
    n = int(input())
    v = list(map(int, input().split()))
    v_even = [v[i] for i in range(0, len(v), 2)]
    v_odd = [v[i] for i in range(1, len(v), 2)]
    even_cnt = sorted(map(list, list(Counter(v_even).items())), key=lambda x: x[1], reverse=True)
    odd_cnt = sorted(map(list, list(Counter(v_odd).items())), key=lambda x: x[1], reverse=True)
    odd_impo = 0
    even_impo = 0
    if len(even_cnt) == 1 and len(odd_cnt) == 1:
        if even_cnt[0][0] == odd_cnt[0][0]:
            if even_cnt[0][1] < odd_cnt[0][1]:
                print((even_cnt[0][1]))
                return

            else:
                print((even_cnt[0][1]))
                return

    if even_cnt[0][0] == odd_cnt[0][0]:
        if even_cnt[0][1] == odd_cnt[0][1]:
            if even_cnt[1][1] < odd_cnt[1][1]:
                odd_impo = 1
                even_impo = 0

            elif even_cnt[1][1] > odd_cnt[1][1]:
                odd_impo = 0
                even_impo = 1

            else:
                odd_impo = 1
                even_impo = 0

        elif even_cnt[0][1] < odd_cnt[0][1]:
            odd_impo = 0
            even_impo = 1

        else:
            odd_impo = 1
            even_impo = 0

    ans = len(v_even) - even_cnt[even_impo][1] + len(v_odd) - odd_cnt[odd_impo][1]

    print(ans)


def __starting_point():
    main()


__starting_point()
