# -*- coding: utf-8 -*-
# @Date    : 2019-08-21 13:24:15
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import sys
sys.setrecursionlimit(10**5 + 1)

inf = int(10 ** 20)
max_val = inf
min_val = -inf


def RW(): return sys.stdin.readline().strip()
def RI(): return int(RW())
def RMI(): return [int(x) for x in sys.stdin.readline().strip().split()]
def RWI(): return [x for x in sys.stdin.readline().strip().split()]


given = input()[::-1]
zeros = 0
lens = len(given)
rets = ''
for i in range(lens):
    if given[i] == '0':
        zeros += 1
        rets += '0'
    elif zeros > 0:
        zeros -= 1
        rets += "1"
    else:
        rets += '0'
rets = rets[::-1]
print(rets)
