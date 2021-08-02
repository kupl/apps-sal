import sys
import math

s = input()

p = '1'
k = 0
v = 1
res = []
for i in s:
    if(p != i):
        p = i
        if(v == 1):
            k = 0
        v = 1
        res.append(p)
    else:
        v += 1
        if(v == 2):
            if(k % 2 == 0):
                res.append(p)
                k = 1
            else:
                k = 0

print("".join(res))
