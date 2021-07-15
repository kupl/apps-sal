from math import *
from random import *
for t in range(int(input())):
    s = input()
    n = len(s)
    p1 = -100000000000
    p2 = p1
    p3 = p1
    otv = 999999999
    for i in range(n):
        if s[i] == '1':
            otv = min(otv, i - min(p2, p3) + 1)
            p1 = i
        if s[i] == '2':
            otv = min(otv, i - min(p1, p3) + 1)
            p2 = i
        if s[i] == '3':
            otv = min(otv, i - min(p2, p1) + 1)
            p3 = i
    if otv > len(s):
        print(0)
    else:
        print(otv)
