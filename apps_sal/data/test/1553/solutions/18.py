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
        return ([int(i) for i in sys.stdin.readline().split()])
    else:
        return (int(sys.stdin.readline()))


n, k = IN()
a = IN()

T = []
M = n
for i in range(n):
    j = BL(T, a[i])
    T[j:j] = [a[i]]
    f = 0
    m = 0
    for g in range(len(T) - 1, -1, -2):
        m += T[g]
    if m > k:
        M = i
        break
print(M)
