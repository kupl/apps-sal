from math import *
import os
import sys
from bisect import *
from io import BytesIO

sys.setrecursionlimit(10 ** 9)

for i in range(int(input())):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = i

    ans = 0
    mx = 0
    for i in range(m):
        if mx < d[b[i]]:
            ans += 2 * (d[b[i]] - i) + 1
            mx = d[b[i]]
        else:
            ans += 1
    print(ans)
