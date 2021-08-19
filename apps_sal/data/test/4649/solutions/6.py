from sys import stdin
from collections import deque
c = int(stdin.readline().strip())
for cas in range(c):
    (n, m) = list(map(int, stdin.readline().strip().split()))
    s = deque(stdin.readline().strip())
    arr = ['R', 'G', 'B']
    ans = n + 3
    for k in range(1):
        for i in range(3):
            x = i
            dp = [0 for i in range(n + 1)]
            for j in range(n):
                if s[j] != arr[x]:
                    dp[j + 1] += 1
                dp[j + 1] += dp[j]
                if j + 1 >= m:
                    ans = min(ans, dp[j + 1] - dp[j + 1 - m])
                x += 1
                x = x % 3
    print(ans)
1
