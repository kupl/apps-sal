import numpy as np
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
dp = np.zeros(k, dtype=np.int64)
dp[0] = 1
for i in range(n):
    a = A[i]
    dp[a:] += dp.copy()[:-a]

ans = 0
for i in range(n):
    a = A[i]
    for j in range(max(0, k - a), k):
        temp = dp[j::-a * 2].sum()
        if j >= a:
            temp -= dp[j - a::-a * 2].sum()
        if temp:
            break
    else:
        ans += 1
print(ans)
