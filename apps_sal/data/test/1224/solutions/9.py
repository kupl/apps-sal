# coding:UTF-8
import sys
from math import log, ceil

MOD = 10 ** 9 + 7
INF = float('inf')

N = int(input())    # 数字

for a in range(1, 41):
    for b in range(1, 31):
        if pow(3, a) + pow(5, b) == N:
            print(("{} {}".format(a, b)))
            return

print(("{}".format(-1)))
