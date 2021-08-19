"""input
9
L0L0LLRR9

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
b = input()
ans = [0 for i in range(10)]
for i in b:
    if i == 'L':
        for i in range(10):
            if ans[i] == 0:
                ans[i] = 1
                break
    elif i == 'R':
        for i in range(9, -1, -1):
            if ans[i] == 0:
                ans[i] = 1
                break
    else:
        temp = int(i)
        ans[temp] = 0
print(''.join([str(i) for i in ans]))
