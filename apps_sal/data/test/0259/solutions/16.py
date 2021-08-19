# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 22:05
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : A. Serval and Bus.py

import math


def main():
    n, t = list(map(int, input().split()))
    ret, best_time = 0, float('inf')
    for i in range(n):
        s, d = list(map(int, input().split()))
        if s < t:
            k = int(math.ceil((t - s) / d))
            s += k * d
        if s < best_time:
            ret = i + 1
            best_time = s
    print(ret)


def __starting_point():
    main()


__starting_point()
