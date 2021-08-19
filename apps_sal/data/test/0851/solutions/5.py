from itertools import permutations, combinations
import sys
from math import *
from fractions import gcd
from random import *


def readints():
    return list(map(int, input().strip('\n').split()))


s = 'abcdefghijklmnopqrstuvwxyz'
(n, k) = readints()
s = input()
lo = -1
hi = n + 1
hop = [0] * n
for i in range(n):
    if s[i] == '0':
        hop[i] = i
    else:
        hop[i] = hop[i - 1]


def test(jump):
    at = 0
    used = 0
    while used < k - 2:
        if at + jump < n:
            to = hop[at + jump]
            if to == at:
                break
            at = to
            used += 1
        else:
            break
    if n - 1 - at > jump:
        return False
    return True


while hi - lo > 1:
    mid = (lo + hi) // 2
    if test(mid):
        hi = mid
    else:
        lo = mid
print(hi - 1)
