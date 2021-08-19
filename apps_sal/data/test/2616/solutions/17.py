import sys
import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
setrecursionlimit(2 ** 20)
MOD = 998244353
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    ind = -1
    for i in range(n):
        if a[i] > 1:
            ind = i
            break
    if ind == -1:
        if n % 2 == 0:
            print('Second')
        else:
            print('First')
        continue
    if ind % 2 == 0:
        print('First')
    else:
        print('Second')
