from itertools import permutations
from functools import lru_cache
N, M = map(int, input().strip().split())
weights = list(map(int, input().strip().split()))
c = []
min_weight = float("inf")
for _ in range(M):
    l, v = map(int, input().strip().split())
    min_weight = min(v, min_weight)
    c.append([l, v])

if min_weight < max(weights):  # we can never pas
    print("-1")
else:
    min_weight = float("inf")
    c.sort()
    for i in range(M - 1, -1, -1):
        min_weight = min(min_weight, c[i][1])
        c[i][1] = min_weight

    @lru_cache(None)
    def bisect(val):
        l, r = 0, M - 1
        while l <= r:
            mid = (l + r) // 2
            if c[mid][1] < val:
                l = mid + 1
            else:
                r = mid - 1
        return c[r][0] if r >= 0 else 0

    def compute(sequence):
        dp = [0] * (N + 1)
        prefix_sum = [0]
        for i in sequence:
            prefix_sum.append(prefix_sum[-1] + weights[i])
        for i in range(2, N + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] + bisect(prefix_sum[i] - prefix_sum[j - 1]))
        return dp[-1]
    base = list(range(N))
    print(min(map(compute, permutations(base))))
