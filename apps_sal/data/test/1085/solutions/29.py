import sys
from bisect import *
from heapq import *
from collections import *
from itertools import *
from functools import *
sys.setrecursionlimit(100000000)


def input():
    return sys.stdin.readline().rstrip()


N = int(input())


def f(x):
    ans = set()
    i = 1
    while i * i <= x:
        if x % i == 0:
            ans.add(i)
        i += 1
    for i in ans.copy():
        ans.add(x // i)
    return ans


ans = set()
for K in f(N) | f(N - 1):
    if K == 1:
        continue
    n = N
    while n % K == 0:
        n //= K
    if n % K == 1:
        ans.add(K)
print(len(ans))
