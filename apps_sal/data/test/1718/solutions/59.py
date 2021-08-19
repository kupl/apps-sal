# coding:UTF-8
import sys
from math import ceil

MOD = 10 ** 9 + 7
INF = float('inf')

N, K = list(map(int, input().split()))     # スペース区切り連続数字
A = list(map(int, input().split()))     # スペース区切り連続数字

res = ceil((N - K) / (K - 1)) + 1
if N <= K:
    res = 1


print(("{}".format(res)))
