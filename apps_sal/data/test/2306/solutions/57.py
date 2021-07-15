import sys

import numpy as np

sys.setrecursionlimit(10000)
INF = float('inf')

N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))

T = np.array(T).cumsum()
V = np.array(V)

va = []
i = 0
for t in np.arange(0, T[-1], 0.5):  # 0.5 区切りの時間
    if t < T[i]:
        va.append(V[i])
    else:
        i += 1
        va.append(min(V[i], V[i - 1]))
va.append(0)

v = 0
for i in range(len(va)):
    va[i] = min(va[i], v)
    v = va[i] + 0.5
v = 0
for i in reversed(list(range(len(va)))):
    va[i] = min(va[i], v)
    v = va[i] + 0.5

print(((np.array(va) / 2).sum()))

