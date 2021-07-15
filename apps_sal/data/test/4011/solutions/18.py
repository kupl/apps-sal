#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Codeforces Round #555 (Div. 3)

Problem B. Long Number

:author:         Kitchen Tong
:mail:    kctong529@gmail.com

Please feel free to contact me if you have any question
regarding the implementation below.
"""

__version__ = '0.2'
__date__ = '2019-04-26'

import sys


def solve(a, f):
    mydict = dict(list(zip(list(map(str, list(range(1, 10)))), f)))
    ans = []
    flag = -1
    for ch in a:
        if mydict[ch] > ch and flag <= 0:
            ans.append(mydict[ch])
            flag = 0
        else:
            ans.append(ch)
            if flag >= 0 and mydict[ch] < ch:
                flag = 1
    return ''.join(ans)

def main(argv=None):
    n = int(input())
    a = list(input())
    f = list(input().split())
    print(solve(a, f))
    return 0

def __starting_point():
    STATUS = main()
    return(STATUS)


__starting_point()
