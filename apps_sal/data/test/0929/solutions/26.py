import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
import string
from bisect import bisect_left
MOD = int(1e9) + 7
INF = float('inf')


def solve():
    n, m = [int(x) for x in input().split()]
    ans = []
    c = 0
    for i in range(n):
        r = [int(x) for x in input().split()]
        for j in range(m):
            if i + 1 == n and j + 1 == m:
                continue
            if i % 2:
                j = m - j - 1
            r[j] += c
            c = r[j] % 2
            if c:
                x = i + 1
                y = j + 1
                if i % 2:
                    if y == 1:
                        ans.append((x, y, x + 1, y))
                    else:
                        ans.append((x, y, x, y - 1))
                else:
                    if y == m:
                        ans.append((x, y, x + 1, y))
                    else:
                        ans.append((x, y, x, y + 1))
    print((len(ans)))
    for r in ans:
        print((*r))


t = 1
for case in range(1, t + 1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
