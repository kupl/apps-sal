# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:33:00 2020

@author: liang
"""
from math import gcd

N, M = map(int, input().split())
A = [int(i) for i in input().split()]

flag = False
res = 1
for a in A:
    a //= 2
    res *= a // gcd(res, a)
    if res > M:
        flag = True
        break
    # print(res)
"""
存在チェック
２で割り切れる個数同じ？
"""

for a in A:
    if int(res / a) == res / a:
        flag = True

if flag:
    ans = 0
    print(ans)
else:
    #ans = (M - res(A)//2)//res + 1
    #ans = (M-1)//res//2 + 1
    ans = (M // res + 1) // 2
    print(ans)
