"""
Created on Wed Sep  9 14:33:00 2020

@author: liang
"""
from math import gcd
(N, M) = map(int, input().split())
A = [int(i) for i in input().split()]
flag = False
res = 1
for a in A:
    a //= 2
    res *= a // gcd(res, a)
    if res > M:
        flag = True
        break
'\n存在チェック\n２で割り切れる個数同じ？\n'
for a in A:
    if int(res / a) == res / a:
        flag = True
if flag:
    ans = 0
    print(ans)
else:
    ans = (M // res + 1) // 2
    print(ans)
