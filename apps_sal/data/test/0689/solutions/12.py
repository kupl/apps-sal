import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
M = 10**9 + 7

T = int(stdin.readline())
# T = 1

for _ in range(T):
    n = int(stdin.readline())
    # n,d = list(map(int,stdin.readline().split()))
    # a = list(map(int,stdin.readline().split()))
    # q = int(stdin.readline())
    # a = list(map(int,stdin.readline().split()))
    # b = list(map(int,stdin.readline().split()))
    # s = stdin.readline().strip('\n')
    d = {}
    for i in range(n):
        s = stdin.readline().strip('\n')
        for c in s:
            if(c not in d):
                d[c] = 0
            d[c] += 1
    res = True
    for c in d:
        if(d[c] % n != 0):
            res = False
            break
    if(res):
        print("YES")
    else:
        print("NO")
