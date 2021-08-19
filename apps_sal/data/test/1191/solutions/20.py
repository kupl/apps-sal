# -*- coding: utf-8 -*-
"""
@Project : CodeForces
@File    : 2.py 
@Time    : 2018/6/17 0:27
@Author  : Koushiro 
"""


def __starting_point():
    n, k = map(int, input().split())
    knight = [[i, 0, 0, 0]for i in range(n)]
    power = list(map(int, input().split()))
    money = list(map(int, input().split()))
    for i in range(n):
        knight[i][1] = power[i]
        knight[i][2] = money[i]
    knight.sort(key=lambda x: x[1])
    yong = []
    yong_sum = 0
    for i in range(n):
        knight[i][3] = knight[i][2] + yong_sum
        if len(yong) < k:
            yong.append(knight[i][2])
            yong.sort()
            yong_sum = sum(yong)
        elif k == 0:
            continue
        else:
            if yong[0] < knight[i][2]:
                yong[0] = knight[i][2]
                yong.sort()
                yong_sum = sum(yong)

    knight.sort(key=lambda x: x[0])
    for i in range(n - 1):
        print(knight[i][3], end="")
        print(" ", end="")
    print(knight[-1][3])


__starting_point()
