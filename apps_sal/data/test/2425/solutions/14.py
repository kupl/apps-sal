# -*- coding: utf-8 -*-
# @Time    : 2019/2/7 22:08
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : C. Meaningless Operations.py

import math

def main():
    num_dict = {
        2: 3,
        3: 1,
        7: 1,
        15: 5,
        31: 1,
        63: 21,
        127: 1,
        255: 85,
        511: 73,
        1023: 341,
        2047: 89,
        4095: 1365,
        8191: 1,
        16383: 5461,
        32767: 4681,
        65535: 21845,
        131071: 1,
        262143: 87381,
        524287: 1,
        1048575: 349525,
        2097151: 299593,
        4194303: 1398101,
        8388607: 178481,
        16777215: 5592405,
        33554431: 1082401,
    }

    q = int(input())
    for _ in range(q):
        a = int(input())
        if a in num_dict:
            print(num_dict[a])
        else:
            temp = int(math.log(a, 2))
            print(pow(2, temp + 1) - 1)

    # for i in range(2, 500):
    #     f = 0
    #     for j in range(1, i):
    #         f = max(f, math.gcd(i ^ j, i & j))
    #     print(i, 'F(A)', f)
    #
    # for k in range(1, 26):
    #     i = pow(2, k) - 1
    #     f = 0
    #     for j in range(1, i):
    #         f = max(f, math.gcd(i ^ j, i & j))
    #     print(i, ':', f, ',')


def __starting_point():
    main()

__starting_point()
