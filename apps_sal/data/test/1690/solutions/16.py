"""input
4
1 1 1 1
"""
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
import heapq
mod = 10 ** 9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n = ri(1)
a = ri()
c = 0
last = 0
ans = 0
ans = [a[-1]]
for i in range(n - 2, -1, -1):
    ans.append(min(ans[-1] - 1, a[i]))
for i in ans:
    if i > 0:
        c += i
print(c)
