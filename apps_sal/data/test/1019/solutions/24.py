from sys import stdout
from random import randint 
from math import *
import re


n = int(input())
mx = 0
mx = mxb = 0
for a in range(1, (n + 1) // 2):
    b = n - a
    t = gcd(a, b)
    if t == 1 and mx < a / b:
        mx = a / b
        mxa = a
        mxb = b

print(mxa, mxb)

