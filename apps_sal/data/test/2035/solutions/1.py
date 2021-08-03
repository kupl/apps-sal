import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import sys

input = sys.stdin.readline
M = mod = 10**9 + 7
def factors(n): return sorted(list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))
def inv_mod(n): return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split(' ')]
def st(): return input().rstrip('\n')
def val(): return int(input())
def li2(): return [i for i in input().rstrip('\n').split(' ')]


n, s1, s2 = li()
l = []
for i in range(n):
    l.append(li())
a1, a2, a3, a4 = [0] * 4

for i in range(n):
    if s1 == l[i][0]:
        if s2 < l[i][1]:
            a2 += 1
        else:
            a4 += 1
    elif s2 == l[i][1]:
        if s1 < l[i][0]:
            a3 += 1
        else:
            a1 += 1
    else:
        if s1 < l[i][0]:
            a3 += 1
        else:
            a1 += 1
        if s2 < l[i][1]:
            a2 += 1
        else:
            a4 += 1
ans = max(a1, a2, a3, a4)
print(ans)
if a1 == ans:
    print(s1 - 1, s2)
elif a3 == ans:
    print(s1 + 1, s2)
elif a2 == ans:
    print(s1, s2 + 1)
else:
    print(s1, s2 - 1)
