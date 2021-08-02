import numpy as np
p = 998244353

N, S = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
dp = np.zeros(S + 1)
dp[0] = 1
for a in A:
    if S < a:
        dp *= 2
        dp %= p
        continue
    tmp = 2 * dp
    dp = np.append(np.zeros(a), dp[:S - a + 1])
    dp += tmp
    dp %= p
print(int(dp[S]))
