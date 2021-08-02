from collections import deque
import math
n, k = list(map(int, input().split()))

a = list(map(str, input().strip()))

ans = 0

dp = [math.inf] * (n + 10)
dp[n + 1] = 0
next = [n + 1] * (n + 10)
now = deque()
for i in range(n):
    if a[i] == '1':
        now.append(i + 1)
    if len(now) == 0:
        continue
    if now[0] + k < i + 1:
        now.popleft()
    if len(now):
        next[i + 1] = now[0]

cur = n + 1
for i in range(n - 1, -1, -1):
    if a[i] == '1':
        cur = i + 1
    if cur - i - 1 <= k:
        next[i + 1] = min(next[i + 1], cur)

for i in range(n, 0, -1):
    dp[i] = min(dp[i], dp[i + 1] + i)
    if next[i] != n + 1:
        dp[max(next[i] - k, 1)] = min(dp[max(next[i] - k, 1)], dp[i + 1] + next[i])

print(dp[1])
