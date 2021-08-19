from sys import stdin
import numpy as np
(N, C) = [int(x) for x in stdin.readline().rstrip().split()]
imos = np.array([[0] * (10 ** 5 + 1) for i in range(C + 1)])
for i in range(N):
    (s, t, c) = [int(x) for x in stdin.readline().rstrip().split()]
    imos[c, s - 1:t] = 1
imos = np.array(imos)
ans = max(imos.sum(axis=0))
print(ans)
