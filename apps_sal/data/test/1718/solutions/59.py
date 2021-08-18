import sys
from math import ceil

MOD = 10 ** 9 + 7
INF = float('inf')

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

res = ceil((N - K) / (K - 1)) + 1
if N <= K:
    res = 1


print(("{}".format(res)))
