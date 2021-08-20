import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


(n, m) = list(map(int, minp().split()))
k = int(sqrt(m))
while k * (k - 1) // 2 > m:
    k -= 1
while k * (k - 1) // 2 < m:
    k += 1
print(max(0, n - m * 2), n - k)
