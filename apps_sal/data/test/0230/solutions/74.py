import random
from collections import defaultdict
from itertools import accumulate
import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
mod = (1 << 61) - 1
base = 1000 + random.randint(0, 100)
power = [1]
for i in range(1, n):
    power.append((power[-1] * base) % mod)
hvalue = [0]
for i in range(n):
    hvalue.append((hvalue[-1] + (ord(s[i]) * power[i])) % mod)


def rollinghash(l, r):
    return ((hvalue[r] - hvalue[l]) * power[n - r]) % mod


def pun(i):
    dc = defaultdict(int)
    if i > n // 2:
        return False
    for j in range(n - i + 1):
        x = rollinghash(j, i + j)
        if dc[x]:
            rg = dc[x]
            if rg <= j:
                return True
        else:
            dc[x] = i + j
    return False


l = 0
r = n // 2 + 1
while l + 1 < r:
    mi = (l + r) // 2
    if pun(mi):
        l = mi
    else:
        r = mi
print(l)
