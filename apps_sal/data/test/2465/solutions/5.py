import sys
from math import gcd
from itertools import groupby as gb
from itertools import permutations as perm
from collections import Counter as C
from collections import defaultdict as dd
sys.setrecursionlimit(10**5)

T = int(input())
for i in range(T):
    ang = int(input())
    g = gcd(ang, 180)
    gg = 180 // g
    a = ang // g
    if gg - a == 1:
        print(gg*2)
    else:
        print(gg)

