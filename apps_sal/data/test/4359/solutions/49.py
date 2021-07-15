import sys
import copy
import math
import itertools
import numpy as np
l = [int(input()) for c in range(5)]
#10で割った余りが1以上で最も小さいものを探す
tmp = 0
cnt = 5
for i in range(5):
    if tmp < 10 - l[i]%10 and l[i]%10!=0:
        tmp = 10 - l[i]%10
        cnt = i
res = 0
for i in range(5):
    if cnt == i:
        res+=l[i]
    else:
        if l[i]%10==0:
            res+=l[i]
        else:
            res+=l[i]+10-l[i]%10

print(res)
