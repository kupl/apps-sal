from collections import defaultdict as DD
from bisect import bisect_left as BL
from bisect import bisect_right as BR
from itertools import combinations as IC
from itertools import permutations as IP
from random import randint as RI
import sys
MOD = pow(10, 9) + 7


def IN(f=0):
    if f == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n = IN(1)
a = IN()
x = a.count(0)
y = a.count(1)
k = 0
(cx, cy) = (0, 0)
for i in range(n):
    if a[i] == 0:
        cx += 1
    else:
        cy += 1
    if cx == x or cy == y:
        k = i
        break
print(k + 1)
