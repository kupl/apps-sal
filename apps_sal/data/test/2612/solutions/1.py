from math import *

for zz in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    dp = [1] * (n + 1)
    for i in range(n - 1, 0, -1):
        j = 2 * i
        while j <= n:
            if a[i - 1] < a[j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)
            j += i

    print(max(dp))
