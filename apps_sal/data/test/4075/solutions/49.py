from itertools import product, repeat
import numpy as np

input_row = lambda: [int(_) for _ in input().split(' ')]

N, M = input_row()
C = np.zeros((M, N), dtype=np.int32)

for i in range(M):
    s = np.array(input_row()[1:])  # ignore k
    C[i, s - 1] = 1  # s_ to zero index.

p = input_row()

all_on_num = 0
for S_ in product(*(repeat([1, 0], N))):
    S = np.array(S_)

    L = C.dot(S) % 2 == p

    if len(L[L == True]) == M:
        all_on_num += 1
print(all_on_num)
