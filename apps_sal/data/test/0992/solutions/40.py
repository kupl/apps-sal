import numpy as np

n, s = list(map(int, input().split()))
a = [int(i) for i in input().split()]

mod = 998244353
dp = np.zeros(s + 1, dtype='i8')
dp[0] = 1
for aa in a:
    tmp = 2 * dp % mod
    tmp[aa:] += dp[:-aa]
    tmp %= mod
    dp = tmp
print((dp[s]))
