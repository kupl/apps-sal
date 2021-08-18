import sys

import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
M = 10**9 + 7

T = int(stdin.readline())

for _ in range(T):
    s = stdin.readline().strip('\n')
    x = int(stdin.readline())
    n = len(s)
    a = [-1] * n
    res = True
    for i in range(n):
        if(s[i] == '1'):
            if((i - x) >= 0 and a[i - x] != 0):
                a[i - x] = 1
                continue
            if((i + x) < n):
                if(a[i + x] == 0):
                    res = False
                    break
                else:
                    a[i + x] = 1
                    continue
            res = False
            break
        else:
            if((i - x) >= 0):
                if(a[i - x] == 1):
                    res = False
                    break
                else:
                    a[i - x] = 0
            if((i + x) < n):
                if(a[i + x] == 1):
                    res = False
                    break
                else:
                    a[i + x] = 0
    ans = ''
    for i in range(n):
        if(a[i] != -1):
            ans = ans + str(a[i])
        else:
            ans = ans + '1'
    if(res):
        print(ans)
    else:
        print(-1)
