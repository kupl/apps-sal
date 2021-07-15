# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 20:42
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : C. Lunar New Year and Number Division.py


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ret = 0
    for i in range(n // 2):
        ret += (a[i] + a[n - i - 1]) ** 2
    print(ret)


def __starting_point():
    main()

__starting_point()
