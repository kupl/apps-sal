
import sys
import os
import math


n = int(input())

if n < 10:
    print(1)
else:
    s = str(n)
    l = len(s)

    v = 10 ** (l - 1)
    w = int(s[1:])

    print(v - w)
