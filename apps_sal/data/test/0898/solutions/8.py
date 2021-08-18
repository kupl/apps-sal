from fractions import gcd
from itertools import combinations, permutations, accumulate
from collections import deque, defaultdict, Counter
import decimal
import re
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7


def readInts():
    return list(map(int, input().split()))


def I():
    return int(input())


n, m = readInts()


def yaku(m):
    ans = []
    i = 1
    while i * i <= m:
        if m % i == 0:
            j = m // i
            ans.append(i)
            if j != i:
                ans.append(j)
        i += 1
    ans = sorted(ans)
    return ans


a = yaku(m)
for i in range(len(a)):
    if n * a[i] <= m:
        ans = a[i]
    else:
        break
print(ans)
