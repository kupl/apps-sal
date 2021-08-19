from collections import deque
from bisect import bisect_left
n = int(input())
a = [int(input()) for _ in range(n)]
dp = deque([])
b = []
for i in range(n):
    j = bisect_left(dp, a[i])
    if j == 0:
        dp.appendleft(a[i])
    else:
        dp[j - 1] = a[i]
print(len(dp))
