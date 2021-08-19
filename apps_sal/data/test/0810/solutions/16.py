from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
#from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))


#def print(x): return sys.stdout.write(str(x)+'\n')
# sys.setrecursionlimit(100000)
mod = int(1e9 + 7)


def check(k):
    while k > 0:
        x = k % 10
        k //= 10
        if x != a and x != b:
            return False
    return True


def fac(n):
    f = [0] * (n + 1)
    f[0] = 1
    for i in range(1, n + 1):
        f[i] = (f[i - 1] * i) % mod
    return f


a, b, n = mdata()
ans = 0
f = fac(n)
for i in range(n + 1):
    k = a * i + b * (n - i)
    if check(k):
        ans = (ans + int(pow(f[i] * f[n - i], mod - 2, mod))) % mod
print((ans * f[n]) % mod)
