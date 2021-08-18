from collections import defaultdict
from heapq import heapify, heappop
n, m, k = map(int, input().split())
items = list(map(int, input().split()))
heapify(items)
items2 = []
for i in range(k):
    items2 += [heappop(items)]
items = items2
offers = defaultdict(lambda: 0)
for i in range(m):
    a, b = map(int, input().split())
    if a <= k:
        offers[a] = max(offers[a], b)
dp = [1e20] * (k + 1)
dp[0] = 0
prefix = [0]
for i in items:
    prefix += [prefix[-1] + i]
for i in range(1, k + 1):
    for j in range(1, i + 1):
        b = offers[j]
        dp[i] = min(dp[i], dp[i - j] + prefix[i] - prefix[i - j + b])
print(dp[-1])
