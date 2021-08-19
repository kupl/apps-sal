import sys
import math
from functools import lru_cache
from itertools import accumulate
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline()[:-1]


def mi():
    return list(map(int, input().split()))


def ii():
    return int(input())


def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


N = ii()
a = list(mi())
l = [0] * (max(a) + 5)
for i in range(N):
    l[a[i]] += 1
    l[a[i] + 3] -= 1
acc = list(accumulate(l))
print(max(acc))
