# coding: utf-8
import math
import copy
import itertools
n = int(input())
flg = False
for i in range(int(math.sqrt(n)) + 1, 0, -1):
    # print(i)
    if n % i == 0:
        a = i
        b = n // a
        flg = True
        break
if flg:
    print(max(len(str(a)), len(str(b))))
else:
    print(len(str(n)))
