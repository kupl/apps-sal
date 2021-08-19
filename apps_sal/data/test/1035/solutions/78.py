"""
Created on Sun Sep 13 14:18:02 2020

@author: liang
"""
import math
from math import gcd
(A, B) = map(int, input().split())
g = gcd(A, B)
n = int(math.sqrt(g))
d_list = list()
for i in range(1, n + 1):
    if g % i == 0:
        j = g // i
        d_list.append(i)
        if j != 1:
            d_list.append(j)
d_list.sort()
ans_list = [1]
d_list.pop(0)
while d_list:
    t = d_list.pop(0)
    ans_list.append(t)
    d_list = [i for i in d_list if i % t != 0]
print(len(ans_list))
