import numpy as np

mod = 998244353

n, s = list(map(int, input().split()))
A = list(map(int, input().split()))
DP = np.zeros(3005, dtype=np.int64)
DP[0] = 1

for a in A:
    double = DP * 2
    double[a:] += DP[:-a]  # shift
    DP = double % mod

print((DP[s]))

