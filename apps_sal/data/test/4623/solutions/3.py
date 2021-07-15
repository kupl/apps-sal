from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush,heappop,heapify
import math
from collections import *
from functools import reduce,cmp_to_key
import sys
input = sys.stdin.readline

from itertools import accumulate

M = mod = 998244353
def factors(n):return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n):return pow(n, mod - 2, mod)
 
def li():return [int(i) for i in input().rstrip('\n').split()]
def st():return input().rstrip('\n')
def val():return int(input().rstrip('\n'))
def li2():return [i for i in input().rstrip('\n')]
def li3():return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    n = val()
    l = li()
    ans = 0
    for j in range(1, 101):
        curr = 0
        m = Counter(l)
        for i in l:
            if j - i != i and m[j - i] and m[i]:
                m[j-i] -= 1
                m[i] -= 1
                curr += 1
            if j - i == i and m[i] > 1:
                m[i] -= 2
                curr += 1
        # print(curr, j)
        ans = max(ans, curr)
    print(ans)
