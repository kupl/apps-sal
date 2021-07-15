# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 20:26
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : C. Ramesses and Corner Inversion.py

def main():
    n, m = map(int, input().split())

    a, b = [], []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        b.append(list(map(int, input().split())))

    for i in range(n - 1):
        for j in range(m - 1):
            if a[i][j] != b[i][j]:
                a[i][j] = 1 - a[i][j]
                a[i + 1][j] = 1 - a[i + 1][j]
                a[i][j + 1] = 1 - a[i][j + 1]
                a[i + 1][j + 1] = 1 - a[i + 1][j + 1]

    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                print('No')
                return
    print('Yes')


def __starting_point():
    main()
__starting_point()
