from sys import stdin as cin
from math import factorial as f
from itertools import combinations as comb
from collections import Counter as C

s = input()
s = s[1:]
n = len(s)
s = s[:n - 1]

m = list(s.split(', '))
if m == ['']:
    print(0)
else:

    # print(m,len(m))
    r = C(m)
    print(len(list(r)))
