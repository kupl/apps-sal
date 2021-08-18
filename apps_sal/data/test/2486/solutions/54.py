import numpy as np
import itertools

N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()


def check(i):
    dp = np.zeros(K, dtype=np.bool)
    dp[0] = True
    for j in itertools.chain(a[:i], a[i + 1:]):
        dp[j:] = np.logical_or(dp[j:], dp[:-j])
    return any(dp[K - a[i]:])


left = -1
right = N
while right - left > 1:
    mid = (right + left) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
