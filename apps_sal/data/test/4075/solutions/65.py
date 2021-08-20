from itertools import product, repeat
import numpy as np


def input_row():
    return [int(_) for _ in input().split(' ')]


(N, M) = input_row()
C = np.zeros((M, N), dtype=np.int32)
for i in range(M):
    s = input_row()[1:]
    for s_ in s:
        C[i, s_ - 1] = 1
p = input_row()
all_on_num = 0
for S_ in product(*repeat([1, 0], N)):
    S = np.array(S_)
    L = C.dot(S) % 2 == p
    L_on = L[L == True]
    all_on = len(L_on) == M
    if all_on:
        all_on_num += 1
print(all_on_num)
