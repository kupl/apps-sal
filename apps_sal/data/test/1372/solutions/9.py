from math import ceil
h, n = list(map(int, input().split()))
data = []
for i in range(n):
    a, b = list(map(int, input().split()))
    data.append([a, b])

max_a = max(a for a, b in data)
dp = [0] * (h + max_a)
for i in range(h + max_a):
    dp[i] = min(dp[i - a] + b for a, b in data)

print((min(dp[h - 1: ]))) 

