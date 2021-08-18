import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [1 for x in range(n + 1)]
    for i in range(n - 1, 0, -1):
        j = i * 2
        cnt = 2
        cur = 1
        while j <= n:
            y = dp[j]
            if arr[j - 1] > arr[i - 1]:
                cur = max(cur, 1 + y)
            cnt += 1
            j = i * cnt
        dp[i] = cur
    ans = max(dp)
    print(ans)
