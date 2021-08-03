import numpy as np
N, S = map(int, input().split())
As = list(map(int, input().split()))

MOD = 998244353

#d = [[0]*3001 for _ in range(3001)]
d = np.zeros((3001, 3001))
d[0, 0] = 1

for i in range(1, N + 1):
    Ai = As[i - 1]
    d[i] += 2 * d[i - 1]
    d[i, Ai:] += d[i - 1][:-Ai]
    d[i] %= MOD
print(int(d[N][S]))
