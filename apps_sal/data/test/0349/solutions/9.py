# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 1:09
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : B. Double Matrix.py


def main():
    n, m = map(int, input().split())
    a, b = [], []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        b.append(list(map(int, input().split())))

    def check(mat, i, j):
        if i > 0 and mat[i][j] <= mat[i - 1][j]:
            return False
        if j > 0 and mat[i][j] <= mat[i][j - 1]:
            return False
        return True

    for i in range(n):
        for j in range(m):
            a[i][j], b[i][j] = min(a[i][j], b[i][j]), max(a[i][j], b[i][j])

    for i in range(n):
        for j in range(m):
            if (not check(a, i, j)) or (not check(b, i, j)):
                print('Impossible')
                return
    print('Possible')


def __starting_point():
    main()


__starting_point()
