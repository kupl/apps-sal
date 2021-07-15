# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 0:35
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : A. Nastya Is Reading a Book.py


def main():
    n = int(input())
    lr = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())

    ret = 0
    for i in range(n):
        if lr[i][1] >= k:
            ret += 1
    print(ret)


def __starting_point():
    main()
__starting_point()
