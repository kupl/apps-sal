# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 20:48
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : B. Lunar New Year and Food Ordering.py


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    price_index = []
    for i in range(n):
        price_index.append((c[i], i))
    price_index.sort()
    # print(price_index)

    ptr = 0
    for _ in range(m):
        t, d = list(map(int, input().split()))
        t -= 1
        cost = 0

        if a[t] > 0:
            served_num = min(a[t], d)
            a[t] -= served_num
            d -= served_num
            cost += served_num * c[t]

        while ptr < n and d > 0:
            _, index = price_index[ptr]
            if a[index] == 0:
                ptr += 1
            served_num = min(a[index], d)
            a[index] -= served_num
            d -= served_num
            cost += served_num * c[index]

        if d > 0:
            print(0)
        else:
            print(cost)


def __starting_point():
    main()

__starting_point()
