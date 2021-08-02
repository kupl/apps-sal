from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline

M = mod = 998244353
def factors(n): return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n): return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n')]
def li3(): return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    i = j = 0
    s = li3()
    n = len(s)
    a = b = c = 0
    ans = float('inf')
    # print(s)
    while j < len(s):
        if s[j] == 1: a += 1
        elif s[j] == 2: b += 1
        else: c += 1
        if a and b and c:
            while i < j:
                if s[i] == 1:
                    if a > 1: a -= 1
                    else: break
                elif s[i] == 2:
                    if b > 1: b -= 1
                    else: break
                else:
                    if c > 1: c -= 1
                    else: break
                i += 1
            ans = min(ans, j - i + 1)
        j += 1
    if ans != float('inf'):
        print(ans)
    else: print(0)
