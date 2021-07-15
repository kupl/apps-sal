import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))
from math import gcd
from math import ceil
from collections import defaultdict as dd, Counter
from bisect import bisect_left as bl, bisect_right as br

t, = I()
while t:
    t -= 1
    a, k = I()
    b = str(a)
    s = []
    while b not in s:
        s.append(b)
        b = str(int(b) + int(min(b)) * int(max(b)))
    if k >= len(s):
        print(s[-1])
    else:
        print(s[k - 1])
