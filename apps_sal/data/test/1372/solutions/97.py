import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

H,N = list(map(int,readline().split()))
m = list(map(int,read().split()))
AB = list(zip(m,m))

INF = 10 ** 18
U = 20000
dp = np.full(U, INF, np.int64)
dp[0] = 0

for a,b in AB:
    n = (U + (-U) % a) // a
    dp = np.resize(dp, U + (-U) % a).reshape(-1,a)
    dp -= (np.arange(n) * b)[:,None]
    dp = np.minimum.accumulate(dp, axis=0)
    dp += (np.arange(n) * b)[:,None]
    dp = dp.ravel()[:U]

answer = min(dp[H:])
print(answer)

