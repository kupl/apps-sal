

import sys
import math


mod = 1000000007


def nospace(l):
    ans = ''.join(str(i) for i in l)
    return ans


n, k = list(map(int, sys.stdin.readline().split(' ')))
for i in range(k):
    if(n % 10):
        n -= 1
    else:
        n = n // 10
print(n)
