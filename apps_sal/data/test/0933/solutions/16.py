import sys
import math
s = input()
l = len(s)
p = '1'
k = 0
v = 1
for i in range(l):
    if p != s[i]:
        p = s[i]
        if v == 1:
            k = 0
        v = 1
        sys.stdout.write(p)
    else:
        v += 1
        if v == 2:
            if k % 2 == 0:
                sys.stdout.write(p)
                k = 1
            else:
                k = 0
