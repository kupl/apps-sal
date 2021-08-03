import numpy as np


def check(x):
    dp = np.zeros(k, np.bool)
    dp[0] = True
    for e in a[:x] + a[x + 1:]:
        dp[e:] |= dp[:-e]

    return dp[-a[x]:].any()


n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

a.sort()

lb = -1
ub = n
while ub - lb > 1:
    m = (lb + ub) // 2
    if check(m):
        ub = m
    else:
        lb = m

print(ub)
