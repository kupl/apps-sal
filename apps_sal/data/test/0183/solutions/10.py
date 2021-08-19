from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline

# M = mod = 998244353


def factors(n): return sorted(list(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))
# def inv_mod(n):return pow(n, mod - 2, mod)


def li(): return [int(i) for i in input().rstrip('\n').split(' ')]
def st(): return input().rstrip('\n')
def val(): return int(input().rstrip('\n'))
def li2(): return [i for i in input().rstrip('\n').split(' ')]
def li3(): return [int(i) for i in input().rstrip('\n')]


def find(a, mod, n):
    rem = n - len(bin(a)[2:])
    ans = 0
    while rem:
        temp = min(rem, 50)
        ans = (ans + 2**temp) % mod
        rem -= temp
    return ans


n, k, m = li()
f = [0 for i in range(k)]
s = 0
for v in range(n):
    tens = 10**v % k
    f = [(sum([f[(j + k - (x + 1) * tens) % k] for x in range(9)]) + f[j]) % m for j in range(k)]
    for x in range(9):
        f[(x + 1) * tens % k] += 1
    if n - v - 1 == 0:
        s += (f[0] % m)
    else:
        s += f[0] * ((10**(n - v - 2) * 9)) % m
    f[0] = 0
print(s % m)
