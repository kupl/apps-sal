import copy
import random
import bisect
import fractions
import math
import sys
import collections
from decimal import Decimal
mod = 10 ** 9 + 7
sys.setrecursionlimit(mod)
d = collections.deque()


def LI():
    return list(map(int, sys.stdin.readline().split()))


(N, X) = LI()
'\nLv i のバーガーの厚みをa[i]\nLv i に含まれるパティの数をp[i]\nとすると\na[0] = 1\na[i] = 2 * a[i-1] + 3\np[0] = 1\np[i] = 2 * p[i - 1] + 1\n\nX = 1 f(N, X) = 0\n\n1 < X <= 1 + a[i - 1]\n一番したのバン\n\n2 + a[i - 1] < X\n一番したのバン\u3000＋\u3000\n'
(a, p) = ([1], [1])
for i in range(N):
    a.append(a[i] * 2 + 3)
    p.append(p[i] * 2 + 1)


def f(N, X):
    if N == 0:
        return 0 if X <= 0 else 1
    elif X <= 1 + a[N - 1]:
        return f(N - 1, X - 1)
    else:
        return p[N - 1] + 1 + f(N - 1, X - 2 - a[N - 1])


print(f(N, X))
