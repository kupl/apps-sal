from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10**20
MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


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
