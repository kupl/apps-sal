
import datetime
from decimal import Decimal, ROUND_DOWN
import heapq
from fractions import gcd
from functools import reduce
from collections import deque
# from math import factorial
import itertools
import collections
import math
import sys
sys.setrecursionlimit(2000000)
# import statistics
# import numpy as np
# n = int(input())
# n, m, p = list(map(int, input().split()))
# a = list(map(int, input().split()))
#
#  abc = [int(input()) for i in range(5)]
# n = int(input())
n, k = list(map(int, input().split()))
# A = list(map(int, input().split()))
# a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# q = int(input())
# p = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
# ab = [list(map(int, input().split())) for i in range(n)]
# print(min(15*n, 100*(n//10+1), 100*(n//10)+15*(n % 10)))

M = 1000000007
f = [1]
g = [1]
for i in range(1, 2 * n + 1):
    f.append(i * f[i - 1] % M)  # 階乗
    g.append(pow(f[i], -1, M))  # f[i]の逆元

for i in range(1, k + 1):
    if n - k < i - 1:
        print((0))
    else:
        a_com = f[n - k + 1] * g[i] % M * g[n - k + 1 - i] % M
        b_com = f[k - 1] * g[i - 1] % M * g[k - i] % M
        print((a_com * b_com % M))
