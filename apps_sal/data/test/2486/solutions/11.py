import numpy as np
import itertools
(N, K) = map(int, input().split())
A = [int(x) for x in input().split()]
A.sort()


def test(i):
    dp = np.zeros(K, dtype=np.bool)
    dp[0] = True
    for a in itertools.chain(A[:i], A[i + 1:]):
        dp[a:] = np.logical_or(dp[a:], dp[:-a])
    return not dp[-A[i]:].any()


left = -1
right = N
while right - left > 1:
    mid = (left + right) // 2
    if test(mid):
        left = mid
    else:
        right = mid
answer = left + 1
print(answer)
