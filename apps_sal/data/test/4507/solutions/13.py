from collections import defaultdict


def input2int():
    return list(map(int, input().split()))


(n, m, k) = input2int()
cost = list(input2int())
cost = sorted(cost)[:k]
preSum = defaultdict(int)
for i in range(k):
    preSum[i] = preSum[i - 1] + cost[i]
preSum[k] = preSum[k - 1]
offer = []
for i in range(m):
    (x, y) = input2int()
    if x <= k:
        offer.append((x, y))
dp = defaultdict(lambda: int(1000000000.0))
dp[0] = 0
for i in range(k + 1):
    if i < k:
        dp[i + 1] = min(dp[i] + cost[i], dp[i + 1])
    for _ in offer:
        (x, y) = _
        if i + x > k:
            continue
        dp[i + x] = min(dp[i + x], dp[i] + preSum[i + x - 1] - preSum[i + y - 1])
print(dp[k])
