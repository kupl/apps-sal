# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 23:26
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : C. Balanced Team.py

from collections import Counter


def main():
    n = int(input())
    a = list(map(int, input().split()))

    counter = Counter()
    for x in a:
        counter[x] += 1

    ret = 0
    for x in a:
        tmp = 0
        for i in range(6):
            tmp += counter[x + i]
        ret = max(ret, tmp)
    print(ret)


def __starting_point():
    main()
__starting_point()
