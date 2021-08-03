import sys

n, k, d = list(map(int, input().split()))
a = [0] + sorted(map(int, input().split()))
dp = [1] + [0] * n
j = k

for i in range(n):
    if dp[i] == 0:
        continue
    j = max(j, i + k)
    while j <= n and a[j] - a[i + 1] <= d:
        dp[j] |= dp[i]
        j += 1

print('YES' if dp[-1] else 'NO')
