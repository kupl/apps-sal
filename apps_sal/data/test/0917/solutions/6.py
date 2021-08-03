# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 1:05
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : A. Zoning Restrictions Again.py


def main():
    n, h, m = list(map(int, input().split()))
    spots = [h] * n
    for _ in range(m):
        l, r, x = list(map(int, input().split()))
        for i in range(l - 1, r):
            spots[i] = min(spots[i], x)
    ret = sum([a ** 2 for a in spots])
    print(ret)


def __starting_point():
    main()


__starting_point()
