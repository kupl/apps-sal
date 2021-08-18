import sys
import numpy as np

sys.setrecursionlimit(10 ** 9)

N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
    B.append([A[i], i])
B.sort(reverse=True)


dp = np.zeros(1, dtype=int)
zero = np.zeros(1, dtype=int)
for act, i in B:
    prev = dp.copy()
    dp = np.append(dp, [0])
    l = len(prev)

    right = np.arange((N - 1 - i) * act, (N - 1 - i) * act - (act * (l)), -act)
    left = np.arange(i * act - (act * (l - 1)), (i + 1) * act, act)
    np.maximum(np.concatenate([prev + left, zero]),
               np.concatenate([zero, prev + right]),
               out=dp)

print(np.max(dp))
