'''input
4 3
4 7
15 1
3 6
6 8
'''
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
import heapq

from heapq import heappush as hp
from heapq import heappop as hhp
mod = 10**9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n, k = ri()
a = []
for i in range(n):
    u, v = ri()
    a.append((v, u))

a.sort(reverse=True)
ans = 0
l = []
cur = 0
pos = 0
while(pos < n):
    if len(l) == k:
        cur -= hhp(l)
    hp(l, a[pos][1])
    cur += a[pos][1]
    ans = max(ans, cur * a[pos][0])
    pos += 1
print(ans)
