import numpy as np
(N, K) = map(int, input().split())
INF = 10 ** 18
A = [0] + [int(x) for x in input().split()] + [INF]
A = np.array(A)
Acum = A.cumsum()
idx = np.searchsorted(Acum, Acum + K)
answer = (N + 1 - idx[:N]).sum()
print(answer)
