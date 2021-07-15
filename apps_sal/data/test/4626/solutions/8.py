from math import *
import os, sys
from io import BytesIO
def f(a, x):
    if a == x:
        return x
    if a > x:
        return a - 1
    else:
        return a + 1
 
#input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
for i in range(int(input())):
    a, b, c = list(map(int, input().split()))
    x = int((a + b + c) / 3 + 0.5)
    a1, b1, c1 = a, b, c
    print(abs(f(a, x) - f(b, x)) + abs(f(c, x) - f(b, x)) + abs(f(a, x) - f(c, x)))
    

