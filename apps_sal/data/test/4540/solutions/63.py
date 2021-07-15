# coding: utf-8
import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
A = np.array([0] + lr() + [0])
diff = np.diff(A)
total = np.abs(diff).sum()
answer = []
for i in range(N):
    answer.append(total - abs(diff[i]) - abs(diff[i+1]) + abs(A[i+2]-A[i]))

print(('\n'.join(map(str, answer))))

