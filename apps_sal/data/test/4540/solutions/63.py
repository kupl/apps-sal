# coding: utf-8
import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


N = ir()
A = np.array([0] + lr() + [0])
diff = np.diff(A)
total = np.abs(diff).sum()
answer = []
for i in range(N):
    answer.append(total - abs(diff[i]) - abs(diff[i + 1]) + abs(A[i + 2] - A[i]))

print(('\n'.join(map(str, answer))))
