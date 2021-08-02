from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline

M = mod = 10**9 + 7
def factors(n): return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
def inv_mod(n): return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split()]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n').split(' ')]
def li3(): return [int(i) for i in input().rstrip('\n')]


n, m = li()
l = []
for i in range(n): l.append(st())
l.sort()
cnt = Counter()
for i in l:
    cnt[i] += 1
toadd = []
d1 = ''
for i in cnt:
    if cnt[i]:
        if i == i[::-1]:
            toadd.append(i * (cnt[i] // 2))
            cnt[i] -= 2 * (cnt[i] // 2)
            if cnt[i] and len(i) > len(d1):
                d1 = i
                cnt[i] -= 1
        elif cnt[i[::-1]]:
            toadd.append(i)
            cnt[i] -= 1
            cnt[i[::-1]] -= 1
        elif i == i[::-1] and len(i) > len(d1):
            d1 = i
            cnt[i] -= 1
s = ''
for i in toadd:
    s += i
s = s + d1 + s[::-1]
print(len(s))
print(s)
