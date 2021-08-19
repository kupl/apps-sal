# coding: utf-8
import sys
import numpy as np
from itertools import permutations


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N, C = lr()
feeling = np.array([lr() for _ in range(C)])
Cij = [lr() for _ in range(N)]
three = [[0] * C for _ in range(3)]
for i in range(N):
    for j in range(N):
        remain = (i + j) % 3
        num = Cij[i][j] - 1
        three[remain][num] += 1

three = np.array(three)
answer = 10 ** 10
for X in permutations(list(range(C)), 3):
    temp = 0
    for i in range(3):
        # X[i]の色にする
        x = X[i]
        y = feeling[:, x]
        temp += (three[i] * y).sum()
    if temp < answer:
        answer = temp

print(answer)
# 13
