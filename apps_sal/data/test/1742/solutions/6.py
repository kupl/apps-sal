# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 11:57
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : D. Nastya Is Buying Lunch.py

import sys

input = sys.stdin.readline


def main():
    n, m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    edge_set = set()
    for _ in range(m):
        u, v = list(map(int, input().split()))
        edge_set.add((u, v))

    ret = 0
    curr_list = [p.pop()]
    while p:
        u = p.pop()
        flag = True
        for v in curr_list:
            if (u, v) not in edge_set:
                flag = False
                break
        if flag:
            ret += 1
        else:
            curr_list.append(u)
    print(ret)


def __starting_point():
    main()


__starting_point()
