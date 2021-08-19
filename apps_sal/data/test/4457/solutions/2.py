"""input
6
5 4 5 4 4 5



"""
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
from heapq import heappush as hpush
from heapq import heappop as hpop
mod = 10 ** 9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n = ri(1)
a = ri()
b = sorted(a, reverse=True)
c = [i + 1 for i in range(n)]
c.sort(key=lambda x: a[x - 1])
c = c[::-1]
ans = 0
x = 0
for i in range(n):
    ans += b[i] * x + 1
    x += 1
print(ans)
print(*c)
