# http://codeforces.com/contest/1154/problem/F
# Explain: https://codeforces.com/blog/entry/66586?locale=en
from collections import defaultdict


def input2int():
    return list(map(int, input().split()))


n, m, k = input2int()
cost = list(input2int())
cost = sorted(cost)[:k]
# cost.reverse()
# print(cost)

preSum = defaultdict(int)
for i in range(k):
    preSum[i] = preSum[i - 1] + cost[i]
preSum[k] = preSum[k - 1]
# print(preSum)

offer = []
for i in range(m):
    x, y = input2int()
    if x <= k:
        offer.append((x, y))

# print(offer)

dp = defaultdict(lambda: int(1e9))
dp[0] = 0

for i in range(k + 1):
    if i < k:
        dp[i + 1] = min(dp[i] + cost[i], dp[i + 1])
    for _ in offer:
        x, y = _
        # print("i: {}, x: {}, y: {}".format(i, x, y))
        if i + x > k:
            continue
        # print('sum: {}'.format(preSum[i + x] - preSum[i + y]))
        dp[i + x] = min(dp[i + x], dp[i] + preSum[i + x - 1] - preSum[i + y - 1])
        # print(dp)

# print(dp)
print(dp[k])

