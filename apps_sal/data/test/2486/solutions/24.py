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
    return not dp[-a[i]:].any()


la = -1
ua = N
while ua - la > 1:
    mid = (ua + la) // 2
    if check(mid):
        la = mid
    else:
        ua = mid

print(ua)
